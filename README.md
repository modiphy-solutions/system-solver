# Implement a quasi-Newton solver for large sparse systems in Python


### Setup:

1. Install Git 

2. Install Python 3.10.x or higher

3. Create a project folder, switch to this folder and create a virtual
   Python environment

```
python3.10 -m venv env
```

4. Activate the environment

Operating system | Run command 
---|---
Windows in Command Shell | `env\Scripts\activate.bat`
Windows in Powershell | `env\Scripts\activate.ps1`
Unix or Linux in bash | `source env/bin/activate`

After activating the environment, Python can be called by `python` (not
`python3` or `python3.10`)

5. Install the NumPy package

```
python -m pip install numpy
```

6. Install the IPython (interactive Python)

```
python -m pip install ipython
```


7. Clone this repository by running

```
git clone https://github.com/modiphy-solutions/system-solver.git
```

The repository will be cloned into a `system-solver` folder


### Run the test file

1. Switch to the `system-solver` subfolder

2. Start up IPython

```
ipython
```

3. Run the test script in IPython

```
run test
```


### References for the Levenberg-Marquardt algorithm

[Levenberg-Marquardt in Matlab](https://www.mathworks.com/help/optim/ug/equation-solving-algorithms.html?searchHighlight=levenberg&s_tid=srchtitle_levenberg_3)


