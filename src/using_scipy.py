import numpy as np
from scipy.optimize import curve_fit


def fit(func, xdata, ydata, yerrordata):
    popt, pcov = curve_fit(func, xdata, ydata, sigma=yerrordata, absolute_sigma=True)
    pstd = np.sqrt(pcov[0][0])
    pci = 1.96 * pstd / np.sqrt(len(xdata))
    return popt[0], pci
