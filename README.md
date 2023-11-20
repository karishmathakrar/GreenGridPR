## Project Overview
GreenGridPR is a project aimed at optimizing the placement of renewable energy installations in Puerto Rico. Leveraging the power of Convolutional Neural Networks (CNN) and Reinforcement Learning (RL), this project seeks to provide insights into the most effective locations for solar and wind energy infrastructures while considering geographical, environmental, and infrastructural constraints. This initiative supports the PR100 goal of transitioning Puerto Rico to 100% renewable energy by 2050.

## Directory Structure
```
/GreenGridPR
|-- /data
|   |-- /pr100
|   |-- /wind_atlas
|   |-- /solar_atlas
|
|-- /src
|   |-- __init__.py
|   |-- /cnn
|   |   |-- __init__.py
|   |   |-- cnn_model.py
|   |   |-- cnn_utils.py
|   |
|   |-- /rl
|   |   |-- __init__.py
|   |   |-- rl_model.py
|   |   |-- rl_utils.py
|   |
|   |-- /preprocessing
|   |   |-- __init__.py
|   |   |-- data_preprocessing.py
|   |
|   |-- main.py
|
|-- /notebooks
|   |-- data_exploration.ipynb
|   |-- model_training.ipynb
|   |-- evaluation.ipynb
|
|-- /tests
|   |-- __init__.py
|   |-- test_cnn.py
|   |-- test_rl.py
|   |-- test_preprocessing.py
|
|-- environment.yml
|-- README.md
|-- .gitignore
```

### Data (/data)
Contains all the datasets used in the project. It includes PR100 data, Wind Atlas data, and Solar Atlas data, each in their respective subdirectories. It also includes the `download_pr100_data.py` script.

### Source (/src)
This directory contains all the source code for the project.

/cnn: Code for the Convolutional Neural Network component.
/rl: Code for the Reinforcement Learning component.
/preprocessing: Scripts for data preprocessing.

### Notebooks (/notebooks)
Jupyter notebooks for exploratory data analysis, model training, and evaluation.

### Tests (/tests)
Contains unit tests for various components of the project.

### environment.yml
YAML file to build the conda environment

## Setup and Running
### Installation
To set up the environment for this project, run:

`conda env create -f environment.yml -p ./environment`

To activate the environment, run:

`conda activate ./environment`

To install `boto3`, which is used to download the PR100 data, run:

`pip install boto3`

To download the PR100 data, navigate to the data directory (`cd data`), and run:

`python download_pr100_data.py`

### Running the Code
To run the main application:
`python src/main.py`

For exploratory data analysis or to see the model training steps, open the Jupyter notebooks in the /notebooks directory.

### Testing
To run tests, navigate to the root directory and execute:
`python -m unittest`
