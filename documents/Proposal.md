## PDSB Project Proposal for Live Cell Fluorescent Imaging

#### The Problem: 
With the drastic breakthrough of microscopy technology over the past decades, live cell imaging becomes a powerful and prevalent tool for many areas of biological research. However, contrary to its wide application, the established tools for processing cell imaging data are relatively limited. There are mainly two challenges for developing automative data processing: one is image stabilization, which is to calibrate the images' coordinates to eliminate the effects of image motions; the other is cell detection, which is to correctly identify and quantify the proper fluorescent cells of interest. Thereby, this project hopes to tackle at least one of these problems, which may improve the quality and efficiency of live cell imaging analysis.

#### The Data:
I will use Calcium imaging of mice's neurons as my data set. These are *in vivo* images of neuronal cells in mouse genicular ganglia. Basically, the mice were engineered in a way that the ganglia neurons would become fluorescent upon activation. The images capture the fluorescence as an indication of neuron firing, while the mice were anesthetized throughout the imaging process. The data are provided by Dr. Charles Zuker's lab on mammalian taste proception at Columbia University Neuroscience Department.

#### The Tools:
I will use python programming for coding, and start with exploring `NoRMCorre`, an algorithm for motion correction, to stabilize the images. I may adopt other packages or tools as well to optimize the process and analyze the data.

#### The Novelty:
Currently based on what I know, most live cell imaging users analyze their images using the `ImageJ` software and its plugins, which are equipped with basic motion correction and fluorescence detection functions. However, its image stabilizer is not always satisfactory. Besides, the fluorescent cells need to be manually selected, and the quantification does not normalize to baseline. This package will hopefully change some of these aspects, which will be a novel improvement.

#### The Goal:
By the end of the semester, I hope to finish implementing a python package for live cell image stabilization, and statistical analysis of fluorescence data. Beyond the due date, I'd like to focus more on programming of fluorescence cell detection, and may learn some machine learning to work on the task. 
