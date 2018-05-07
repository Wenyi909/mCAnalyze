## MCAnalyze Library
### Live Cell Imaging Motion Correction Analysis
MCAnalyse is a python library built on the basis of the `CaImAn` package. `CaImAn` enables two different motion corrections for live cell imaging: rigid motion correction and non-rigid motion correction. `MCAnalyze` performs quality analysis and comparison between the two motion corrections to help users decide which algorithm is a better match for their imaging file.

#### Installation
1. Download the `CaImAn` package, and create a `caiman` conda environment, following the instructions from the [[link]](https://github.com/flatironinstitute/CaImAn/). 
2. Download the `MCAnalyze` package by running the following command in the terminal:
   ```
   git clone https://github.com/Wenyi909/mCAnalyze
   ```
3. Run the following commands in the terminal to start the installation:
   ```
   source activate caiman
   conda install notebook ipykernel
   ipython kernel install --user
   pip install caiman
   pip install mCAnalyze
   ```
4. Now you are done with installation. You can go to the notebooks directory for testing the functions of the library in the `demo-MCAnalyze.ipynb` notebook. You can go to `NoRMCorre.ipynb` to see how motion correction is performed by `CaImAn` package.

#### Download File
Unfortunately, due to the size of the demo file, the original imaging data for demo cannot be uploaded to the github. But the file is shared on google drive with anyone with lionmail. 

In order to download the demo file, go to the [[link]](https://drive.google.com/file/d/1aQTiI7U2RznnVqTZjYVrLmyJ9MSC-ldt/view). You can store the demo file in the `data` directory.

#### Test the Library
Go to `notebooks/demo-MCAnalyze.ipynb` for testing the functions. Note that you need to be in the `caiman` environment before starting the notebook.

