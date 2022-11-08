## VirtualEnv and Binder

Let us assume that you want to install some research code to either use it or test the results. It might use an older version of a particular package that you have already installed. 

One option is to create a virtual environment using 

Virtualenv is a Python package to create isolated Python environments and can be installed through pip, the Python package manager: ```pip install virtualenv``` or ```pip3 install virtualenv``` (if using Python 3). 

This is a simple way of creating a Python environment. Replace the word ENVIRONMENT with the name that you want to call the environment. The -p option will link to your machine's python3 executable.

```virtualenv -p python3 ENVIRONMENT```

When it is created, then start the environment using

```source ENVIRONMENT/bin/activate```

This starts the isolated environment so that you can install the required pacakges and develop it without affecting other pieces of code. 

Once you have developed the code, you can save the package requirements using pip

```(ENVIRONMENT)  pip freeze > requirements.txt```

This will save the packages used and the current version into a text file. The file should be added to your repository to help others install it. 

If you have downloaded or cloned a repository and started a virtual environment, then you can start the environment and install the requirements using:

```(ENVIRONMENT)  pip install -r requirements.txt```

This will install the packages and versions. You can, manually, remove the package versions from the requirements, but this leaves you open to having different versions of packages on different machines. 

It is a choice. The pinning of packages to certain versions can cause issues when Python is upgraded and a version is no longer supported. However it does mean that the same version is in use for the project and could be upgraded at some point. 

## Binder

Binder is a service that can run Jupyter notebooks online and uses the requirements.txt file from pip freeze to load the modules.