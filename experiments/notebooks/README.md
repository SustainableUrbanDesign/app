# SUDS notebooks
This folder contains experimental notebooks for the SUDS projects. Code here may end up as part of the SUDS platform.

## Installation
This project relies on [Conda](https://www.anaconda.com/products/individual) for dependency management. This is mainly due to the complexity of installing the Python geospatial tools, such as GDAL.

Make sure Conda is installed on your operating system and then run the following command from within this project directory.

```
conda env create -f environment.yml
```

## Activation
After installing the project dependencies, run the following command to activate the environment.

```
conda activate suds-notebooks
```

## Running
Once the environment is activated, you can run the JupyterLab project in order to access these notebooks.

```
jupyter lab
```