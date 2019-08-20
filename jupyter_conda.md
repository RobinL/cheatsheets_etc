To control where you want conda environments installed, run the following command on the terminal.  If you're working on the analytical platform, this needs to be set because otherwise your environments will be written to `/opt/conda` rather than your home directory, and therefore will be lost every time your Jupyter pod restarts.

```
echo "envs_dirs:
  - /home/jovyan/.conda/envs" > /home/jovyan/.condarc
```

First you need to set up a conda environment using `conda create --name myenv python=3.7` (or whatever version of python you want).  See https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html for more info
**

Activate the environment using `conda activate myenv`

Then, you need to install `ipykernel` within this environment using `conda install ipykernel`

Then you need to map this to a jupyter kernel so you can start Jupyter Notebooks within the conda environment.

To do this, type `python -m ipykernel install --user --name my_env --display-name "My env"` at the terminal, with the `myenv` conda environment activated.

To install new packages into the environment, make sure the conda environment is activated:

`conda activate myenv`

`conda install numpy`

Then choosing the ‘My Venv’ kernel for your notebooks (can take a few seconds to appear, sometimes seems to need you to shut down all running notebooks+terminals).    

Within your notebook, check that your environement is working e.g with `import sys; sys.version` or try importing a package such as `pandas` which you know exists in the base environment but shouldn't exist within the conda env.  (`pd.__file__` will tell you where the import is coming from)

When you need to freeze/export the dependencies of your environment, you can do this on the command line.  Make sure your environement is activated and then `conda env export > environment.yml`.  You can then use this e.g. to build a Docker image of this environment.
