# Machine Learning Project Template
**V1.3**

Here is where you should have the description of the project

### What is in this reporitory? 
1. Some things about the project

## Setup steps
Use the **Use this template** button to create a new repository from this one

**Tested on:** 
* Ubuntu 18.04 with Nvidia K80
    * Azure Data Science Virtual machine template
* Ubuntu 20.04 with Nvidia GEFORCE RTX 2070 SUPER

NOTE: Both setups assume that your your CUDA and GPU drivers work if not check troubleshooting below

#### Option 1: Anaconda (recommended)
1. Install Anaconda
2. Initialize conda environment ```conda create -n <env name>```
3. Activate conda environment ```conda activate <env name>```
4. Installing packages
   1. Install via conda ```conda install -c conda-forge -c bioconda --file=requirements_manual.txt``` (If this doesn't work then try 4.2)
   2. Install via pip - Follow Option 2 from this step 
5. If your machine has a supported GPU (list here) then ```pip3 install --user install tensorflow-gpu```
6. Setup DVC and other libraries ``` chmod 755 setup.sh; ./setup.sh ```

#### Option 2: Directly on machine
1. Install requirements ``` pip3 install --user -r requirements_manual.txt ```
2. If your machine has a supported GPU (list here) then ```pip3 install --user install tensorflow-gpu```
3. Setup DVC and other libraries ``` chmod 755 setup.sh; ./setup.sh ```


### Tools in this repository and recommended toolset

- Data versioning: [DVC](https://www.dvc.org)
- Model versioning + Training monitoring + Hyperparameter sweeps: [Weights and Biases](https://www.wandb.com/) - Please signup first
- Distributed training: [Ray (Tune)](https://ray.io/) OR Weights and Biases
- Coding: [JupyterLab](https://jupyter.org/) or if you want free GPUs and data privacy isn't an issue [Colab](http://colab.research.google.com/)
- Training framework: [Tensorflow](https://tensorflow.org) + [Keras](https://keras.io/)
- Tabular data management: [Pandas](https://pandas.pydata.org/)
- Plotting: [Matplotlib](https://matplotlib.org/) [Plotly](https://plotly.com/python/)


### Setup guides and docs
**DVC**
1. DVC will be initalized by default in the root directory via the setup.sh
2. Rest of the data versioning guide can be found here: https://dvc.org/doc/start/data-versioning

**Ray (Tune)**
1. Ray is already installed so first you will need to setup a training cluster or setup your experiment management
2. [Guide here to setup cluster training](https://docs.ray.io/en/master/tune/tutorials/tune-distributed.html#tune-distributed)
3. [Guide here to setup parallel training on one machine](https://docs.ray.io/en/master/tune/tutorials/tune-usage.html#parallelism-gpus) 

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
1. Check which GPU you have
2. Check if you have installed the correct version of tensorflow-gpu for the drivers + CUDA installed 
3. Check if you also have the right version of CUDA installed for tensorflow-gpu
4. If nothing works try a pre-built VM template on the cloud


