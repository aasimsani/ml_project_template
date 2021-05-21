# Machine Learning Project Template
**V1.4**

Here is where you should have the description of the project

### What is in this reporitory? 
1. Some things about the project

## Setup steps
Use the **Use this template** button to create a new repository from this one

**Tested on:** 
* Ubuntu 18.04 with Nvidia K80
    * Azure Data Science Virtual machine template
* Ubuntu 18.04 with Nvidia V100
* Ubuntu 20.04 with Nvidia GEFORCE RTX 2070 SUPER

NOTE: Both setups assume that your your CUDA and GPU drivers work if not check troubleshooting below

#### Option 1: Anaconda (recommended)
1. Install Anaconda
2. Initialize conda environment ```conda create -n <env name>```
3. Activate conda environment ```conda activate <env name>```
4. Installing packages
   1. Installing via conda
    - No GPU ```conda install -c pytorch -c conda-forge -c bioconda --file=requirements_conda.txt``` (If this doesn't work then try 4.2)
    - With GPU support ```conda install -c pytorch -c conda-forge -c bioconda --file=requirements_conda_gpu.txt``` (If this doesn't work then try 4.2)
   2. Install via pip - Follow Option 2 from this step 
5. Setup DVC and other libraries ``` chmod 755 setup.sh; ./setup.sh ```

#### Option 2: Directly on machine
1. Install requirements ``` pip3 install --user -r requirements.txt ```
2. Setup DVC and other libraries ``` chmod 755 setup.sh; ./setup.sh ```


### Tools in this repository and recommended toolset

- Data versioning: [DVC](https://www.dvc.org)
- Model versioning + Training monitoring + Hyperparameter sweeps: [Weights and Biases](https://www.wandb.com/) - Please signup first
- Distributed training: Weights and Biases
- Coding: [JupyterLab](https://jupyter.org/) or if you want free GPUs and data privacy isn't an issue [Colab](http://colab.research.google.com/)
- Training framework: [Pytorch](http://pytorch.org/) + [PyTorchLightning](https://www.pytorchlightning.ai/)
- Tabular data management: [Pandas](https://pandas.pydata.org/)
- Plotting: [Matplotlib](https://matplotlib.org/) [Plotly](https://plotly.com/python/)


### Setup guides and docs
**DVC**
1. DVC will be initalized by default in the root directory via the setup.sh
2. Rest of the data versioning guide can be found here: https://dvc.org/doc/start/data-versioning

**Weights and Biases**
1. To setup Weights and biases first sign up and create a project or get added to the project
2. Login via terminal and add Weights and Biases to start. [Instructions here](https://docs.wandb.com/quickstart)
3. [How to log Keras data?](https://docs.wandb.com/library/integrations/keras)
4. [How to integrate Ray Tune with Weights and Biases?](https://docs.wandb.com/library/integrations/ray-tune)
5. [How to use built-in hyperparameter sweep functionality?](https://docs.wandb.com/sweeps)

**Jupyter Lab**
1. Starting Jupyterlab ```jupyter lab```
2. [User guide, key mapping and shortcut customization](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)

### Troubleshooting

**No Python3 Kernel in Jupyter Lab**

Solve by doing the following:

1. ``` python3 -m pip install ipykernel ```
2. ``` python3 -m ipykernel install --user ```
3. Restart Jupyter Lab

**DVC/Tensorboard/JupterLab command not found**
1. ``` python3 -m <command here> ```
2. Issue with python versions on the machine

**Can't access jupyter from local machine after cloud deployment**
1. Run Jupyter Lab ```jupyter lab --no-browser --ip=0.0.0.0 --port=8888```


**GPU driver/ tensorflow-gpu issues**
1. Check which GPU you have on the machine and [make sure it's supported](https://developer.nvidia.com/cuda-gpus)
2. Install CUDA if you don't have it installed the best way to do this is to just do ```conda install tensorflow-gpu``` and it should take care of itself.
3.If the above doesn't work check if you have installed the correct version of [tensorflow-gpu for installed CUDA drivers](https://www.tensorflow.org/install/source#gpu). ```nvidia-smi```
4. Check which version of GPU drivers are needed for the GPU and the supported CUDA versions for the drivers from [here](https://docs.nvidia.com/deploy/cuda-compatibility/index.html).
5. When you have found the right version follow this [guide](https://medium.com/@exesse/cuda-10-1-installation-on-ubuntu-18-04-lts-d04f89287130) and replace the CUDA driver files in the commands with the right versions. 
5. If nothing works try a pre-built VM template on the cloud


