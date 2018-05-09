#!/usr/bin/env python

# import image processing tools
import cv2
import caiman as cm
from caiman.motion_correction import MotionCorrect, tile_and_correct,\
    motion_correction_piecewise

# import analyzing, plotting tool
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class MCAnalyze:
    """
    Returns a McAnalyze class instance with rigid and non-rigid motion\
    correction information presented in plots and panda DataFrame.

    Parameters:
    -----------
    file_name: str
        path to file to motion correct

    max_shifts: tuple
        maximum allowed rigid shift

    strides: tuple
        intervals at which patches are laid out for NoRMCorre

    overlaps: tuple
        overlap between pathes (size of patch strides + overlap)

    upsample_factor_grid: int
        upsample factor of shifts per patches to avoid smearing when\
        merging patches

    max_deviation_rigid: int
        maximum deviation allowed for patch with respect to rigid shift

    Attributes:
    -----------
    name_orig: path name of the original data as a list

    name_rig: path name of the rigid corrected data as a list

    name_pwrig: path name of the rigid corrected data as a list

    data_orig: movie of the original imaging data

    data_rig: movie of the rigid movement corrected data

    data_pwrig: movie of the non-rigid movement corrected data

    shifts_rig: pixel shifts of rigid motion correction

    x_shifts_pwrig: pixel shift in x direction of non-rigid correction

    y_shifts_pwrig: pixel shift in y direction of non-rigid correction
    """
    def __init__(self, file_name, max_shifts, strides, overlaps,
                 upsample_factor_grid, max_deviation_rigid):
        self.name_orig = [file_name]
        self.data_orig = cm.load_movie_chain(self.name_orig)
        
        self.name_rig, self.name_pwrig, self.shifts_rig, self.x_shifts_pwrig, self.y_shifts_pwrig, self.template_shape = self._run_motion_correction(
                file_name, max_shifts, strides, overlaps,
                upsample_factor_grid, max_deviation_rigid)

        self.data_rig = cm.load(self.name_rig)
        self.data_pwrig = cm.load(self.name_pwrig)

    def _run_motion_correction(self, file_name, max_shifts, strides, overlaps,
                               upsample_factor_grid, max_deviation_rigid):
        """
        Private function that initiates motion correction from CaImAn package,
        and return the motion corrected file names and their respective pixel
        shifts.
        """

        offset_orig = np.nanmin(self.data_orig[:1000])
        G6Image = MotionCorrect(
            file_name, offset_orig, max_shifts=max_shifts,
            niter_rig=1, splits_rig=56, strides=strides,
            overlaps=overlaps, splits_els=56,
            upsample_factor_grid=upsample_factor_grid, shifts_opencv=True,
            max_deviation_rigid=max_deviation_rigid, nonneg_movie=True)

        G6Image.motion_correct_rigid(save_movie=True)

        G6Image.motion_correct_pwrigid(save_movie=True,
                                       template=G6Image.total_template_rig)
        name_rig = G6Image.fname_tot_rig
        name_pwrig = G6Image.fname_tot_els
        shifts_rig = G6Image.shifts_rig
        x_shifts_pwrig = G6Image.x_shifts_els
        y_shifts_pwrig = G6Image.y_shifts_els
        template_shape = G6Image.total_template_els.shape

        return name_rig, name_pwrig, shifts_rig, x_shifts_pwrig, y_shifts_pwrig, template_shape

    def _border_correction(self):
        """
        Private function that performs border correction.
        """
        bord_px_rig = np.ceil(np.max(self.shifts_rig)).astype(np.int)
        bord_px_pwrig = np.ceil(np.maximum(np.max(np.abs(
            self.x_shifts_pwrig)), np.max(np.abs(self.y_shifts_pwrig)))).astype(np.int)
        bord_px = np.maximum(bord_px_rig, bord_px_pwrig)

        return bord_px

    def _run_matrics_computation(self, name):
        """
        Private function that initiates motion correction matrics computation
        from the CaImAn package.
        """

        final_size = np.subtract(self.template_shape,
                                 2 * self._border_correction())

        tmp, corr, flow, norm, smooth = cm.motion_correction.compute_metrics_motion_correction(
            name[0], final_size[0], final_size[1],
            swap_dim=False, winsize=100, play_flow=False,
            resize_fact_flow=0.2)
        
        return tmp, corr, flow, norm, smooth

    def play_all_movies(self):
        """
        Public function that plays the original data, rigid corrected and
        non-rigid data file side by side for comparison.
        """

        offset_orig = np.nanmin(self.data_orig[:1000])
        offset_rig = np.min(self.data_rig[:1000])
        offset_pwrig = np.nanmin(self.data_pwrig[:1000])

        cm.concatenate([self.data_orig.resize(0.6, 0.6, 0.2)-offset_orig,
                        self.data_rig.resize(0.6, 0.6, 0.2)-offset_rig,
                        self.data_pwrig.resize(0.6, 0.6, 0.2)-offset_pwrig],
                       axis=2).play(gain=1.5, offset=0,
                                    bord_px=self._border_correction())
        return self

    def compare_correction(self):
        """
        Public function that compares motion correction performances and
        returns graphs, plots, and dataframe as analysis.
        """

        print("Start pixel shift comparison...")

        x_shifts_rig = np.array(self.shifts_rig)[:, 0]
        y_shifts_rig = np.array(self.shifts_rig)[:, 1]

        x_shifts_pwrid = np.array(self.x_shifts_pwrig)
        y_shifts_pwrid = np.array(self.y_shifts_pwrig)

        pixel_graph = plt.figure(figsize=(20, 5))

        plt.subplot(2, 2, 1)
        plt.title("Rigid Movement Correction")
        plt.plot(x_shifts_rig)
        plt.ylabel("x shifts (pixels)")

        plt.subplot(2, 2, 3)
        plt.plot(y_shifts_rig)
        plt.ylabel("y shifts (pixels)")
        plt.xlabel("frame")

        plt.subplot(2, 2, 2)
        plt.title("Non-rigid Movement Correction")
        plt.plot(x_shifts_pwrid)
        plt.ylabel("x shifts (pixels)")

        plt.subplot(2, 2, 4)
        plt.plot(y_shifts_pwrid)
        plt.ylabel("y shifts (pixels)")
        plt.xlabel("frame")

        plt.suptitle("Pixel Shift Comparison", fontsize=16)

        print("done pixel shifts!")

        print("Start matrics comparison...")
        print("Run matrics computation (take a while, please be patient)...")

        t_orig, corr_orig, f_orig, n_orig, crisp_orig = self._run_matrics_computation(self.name_orig)

        t_rig, corr_rig, f_rig, n_rig, crisp_rig = self._run_matrics_computation(self.name_rig)

        t_pwrig, corr_pwrig, f_pwrig, pw_orig, crisp_pwrig = self._run_matrics_computation(self.name_pwrig)

        print("Done matrics computation!")

        corr_graph = plt.figure(figsize=(10, 5))
        plt.suptitle("Correlation with Template Comparison", fontsize=16)

        plt.subplot(2, 1, 1)
        plt.plot(corr_orig)
        plt.plot(corr_rig)
        plt.plot(corr_pwrig)
        plt.legend(["Original", "Rigid", "Non-rigid"])
        plt.ylabel("Correlation")

        plt.subplot(2, 1, 2)
        plt.plot(corr_rig)
        plt.plot(corr_pwrig)
        plt.legend(["Rigid", "Non-rigid"])
        plt.ylabel("correlation")
        plt.xlabel("frame")

        minCorr = min([min(corr_orig), min(corr_rig), min(corr_pwrig)])

        corr_scatter = plt.figure(figsize=(12, 3))

        plt.subplot(1, 3, 1)
        plt.scatter(corr_orig, corr_rig)
        plt.xlabel("original")
        plt.ylabel("rigid")
        plt.plot([minCorr, 1.0], [minCorr, 1.0], "r--")
        plt.axis("square")

        plt.subplot(1, 3, 2)
        plt.scatter(corr_orig, corr_pwrig)
        plt.xlabel("original")
        plt.ylabel("non-rigid")
        plt.plot([minCorr, 1.0], [minCorr, 1.0], "r--")
        plt.axis("square")

        plt.subplot(1, 3, 3)
        plt.scatter(corr_rig, corr_pwrig)
        plt.xlabel("rigid")
        plt.ylabel("non-rigid")
        plt.plot([minCorr, 1.0], [minCorr, 1.0], "r--")
        plt.axis("square")

        df = pd.DataFrame({"max x shifts": ["NaN", np.max(x_shifts_rig),
                                            np.max(x_shifts_pwrid)],
                           "max y shifts": ["NaN", np.max(y_shifts_rig),
                                            np.max(y_shifts_pwrid)],
                           "min correlation": [min(corr_orig),
                                               min(corr_rig),
                                               min(corr_pwrig)],
                           "crispiness": [int(crisp_orig), int(crisp_rig),
                                          int(crisp_pwrig)]},
                          index=["Original", "Rigid", "Non-rigid"])
        return pixel_graph, corr_graph, corr_scatter, df





































