from scipy.optimize import curve_fit


def fit(func, xdata, ydata, yerrordata):
    popt, pcov = curve_fit(func, xdata, ydata, sigma=yerrordata, absolute_sigma=True)
    return popt[0], pcov[0][0]
