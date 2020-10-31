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

## Using Git and Github

If you prefer to use a GUI for using git I recommend looking at [SourceTree](https://www.sourcetreeapp.com/)

### Install Git

[git installation instructions](https://www.atlassian.com/git/tutorials/install-git)

Refer to the side bar on the left for instructions on how to install git on your platform.

Open a terminal (Mac) or PowerShell (Windows) and type in `git --version` to verify that git is installed on your system.

To clone the repository use the command:

`git clone git@github.com:cwperks/eai6000_group5.git`

Once the repository is cloned navigate into the repository using (`cd` is short for `change directory`).

`cd eai6000_group5`

From here the repository is ordered by week.

```
eai6000_group5
│   README.md
│   requirements.txt    
|   .gitignore
│
└───week1
│   │   group5_week1_eda.ipynb
│   │   group5_week1_assignment.md
│   
└───week2
    │   group5_week2_notebook.ipynb
    │   group5_week2_assignment.md
```

### Pulling Changes

To get the latest changes on the `main` branch. Use the command `git pull`. It is best practice to `git pull` before you make a commit in case any teammates any changes in the repository that you have not pulled locally. 

If you are interested in getting to know more about branching I recommend reading this post on [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20Workflow%20is%20a%20Git,designed%20around%20the%20project%20release.&text=In%20addition%20to%20feature%20branches,%2C%20maintaining%2C%20and%20recording%20releases.)

Branches are great ways of making sure changes don't have conflicts in git. We may not be using branches, but as you use git more as a software or data engineer they become imperative when working collaboratively. `Pull Requests` are requests on merging branches back into the `main` branch on git and come built in with a code review feature.

### Pushing Changes

1) Add the changes

```
git add .

or

git add <filename>
```

2) Run `git status` to see the changes to be committed. Unadded changes will show in <span style="color:red">red</span> and added changes will show in <span style="color:green">green</span>.

3) Commit the change: 

```
git commit -m "Add your commit message here."
```

The commit message is what shows when you look at all commits in github or when you run the git log command

4) Push the change:

```
git push

or

git push origin main
```

In `git push origin main`:

- origin is the alias of the remote repository. Its short for `git@github.com:cwperks/eai6000_group5.git`
- `main` is the branch to push to. If you leave out `origin main` that is what git will default to. You may also hear developers refer to this branch as `master`. `master` is still the term used in Github enterprise, but it was changed on Github. 

### Full example of git push

```
git add README.md
git commit -m "Update README with steps to git push and pull"
git push origin main
```

## Overview

Our group has selected the *Credit Card Transactions Fraud Detection Dataset* to run an analysis on financial transactions and identity fraudulent transactions. The dataset can be found on [Kaggle](https://www.kaggle.com/kartik2112/fraud-detection).