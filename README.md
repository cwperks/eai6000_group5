# Group 5

##### Noelani Roy, Yihong Qiu, Cosimo Cambi, Craig Perkins

## Prerequisites

This repository keeps track of dependencies using [virtualenv](https://virtualenv.pypa.io/en/latest/). `virtualenv` is a tool to create isolated Python environments. 

To install pip run: `pip install virtualenv`

Create a virtualenv in the root level of the repository. To create a virtual environment run `virtualenv env`.

This command creates a directory called `env` in the directory you are currently in and this will not be tracked by git due to being ignored in the `.gitignore` file.

To activate the virtual environment run: `source env/bin/activate`

If the command above is successful your terminal should be preceded with `(env)`.

To deactivate the virtual environment run: `deactivate`

### Install Dependencies

Run `pip3 install -r requirements.txt`

If you install new packages via pip please update the `requirements.txt` using the command: `pip freeze > requirements.txt`

## Overview

Our group has selected the *Synthetic Financial Datasets For Fraud Detection* dataset to run an analysis on financial transactions and identity fraudulent transactions. The dataset can be found on [Kaggle](https://www.kaggle.com/ntnu-testimon/paysim1).