# MLOps

This is the repository for the labs/tutorials of the lecture Machine Learning Operations (MLOps), ZHAW BSc Computer Science & Data Science.

## Setup

- install Anaconda (https://www.anaconda.com/download/) or Miniconda (https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)



e.g. for Windows with WSL2:
```
# find latest version from https://repo.anaconda.com/archive/ and download
wget https://repo.continuum.io/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
# install 
bash Anaconda3-2023.09-0-Linux-x86_64.sh

```




- create conda environment and install pytorch, jupyer notebook and dependencies


```
# create environment
conda create -n mlops_labs python=3.11 
# activate environment
conda activate mlops_labs
# install pytorch (stable, windows, cpu)
conda install pytorch torchvision torchaudio cpuonly -c pytorch
# install jupyter notebook
pip install notebook
# install dependencies
conda install matplotlib
```


- goto local folder where you checked out the repo, e.g. 

```
cd (...)/MLOps_BSc/lab01

```

- start jupyter notebook locally

```
jupyter notebook
```
or, to skip token or password auth
```
jupyter notebook --NotebookApp.token='' --NotebookApp.password=''
```

- open jupyter in browser

http://localhost:8888

- open intended notebook by clicking on the corresponding file

