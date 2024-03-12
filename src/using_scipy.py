import numpy as np
from scipy.optimize import curve_fit


def fit(func, xdata, ydata, yerrordata):
    popt, pcov = curve_fit(func, xdata, ydata, sigma=yerrordata, absolute_sigma=True)
    perr = np.sqrt(pcov[0][0])
    return popt[0], perr
