# Finding the temperature of the CMB with data from the FIRAS experiment

## Installing requirements

If you are installing directly in your system, you can use:
```
pip install -r requirements.txt
```

If you are using a virtual environment, you can use:
```
pip freeze > requirements.txt
```

## How to use the script

1. Make sure you are in the `src` folder.
2. Run `main.py`, ensuring you have all the other script files (`choosing_methods.py`, `using_scipy.py`, `own_algorithm.py`) as code is distributed between each.
3. You will be prompted about various options to choose what the program will do. Below is a list of each.

## Options

### Main method
You will first be asked to choose which method you want the program to use for the calculations. The options are the following:
- "own" - use an algorithm coded by me
- "scipy" - use curve_fit function from the scipy library
- "both" (default) - use both methods

### Sampling method
If you choose "own" or "both", you will be prompted about the sampling method you want the program to use. The options are the following:
- "uniform" (default) - sample possible temperature values uniformly from the interval [0, 293.15] K - minimum possible temperature and NTP temperature

### Minimizing method
Again, if you choose "own" or "both" for the main method, you will be prompted about which error minimizing method you want the program to use. The options are the following:
- "rms" (default) - root mean square error

## Explaining the results

The results are given in the form of the fitted value made by the chosen method(s), as well as the corresponding error, and a plot.

The errors of the data points are the ones given in the data set and are displayed as vertical lines.

The error of the fitted value for both algorithms are one standard deviation. These errors are displayed as a shaded area the same color as the prediction lines.
