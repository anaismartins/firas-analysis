import numpy as np


def rms(n, data, prediction):
    sum = 0
    for i in range(n):
        sum += (data[i] - prediction[i]) ** 2

    return np.sqrt(sum / n)


def fit(
    func,
    xdata,
    ydata,
    yerrordata,
    min=0,
    max=293.15,
    sampling_method="uniform",
    minimizing_method="rms",
    target_error=1e-5,
    max_iterations=1e10,
):
    min_error = np.inf
    best_T = 0

    for i in range(max_iterations):

        # sampling for T
        if sampling_method == "uniform":
            T = np.random.uniform(min, max)
        elif sampling_method == "normal":
            T = np.random.normal(3)
            if T < min or T > max:
                continue

        # calculating the prediction for the spectrum
        try:
            prediction = func(xdata, T)
        except ZeroDivisionError:
            continue

        # calculating the error
        if minimizing_method == "rms":
            error = rms(len(xdata), ydata, prediction)
        elif minimizing_method == "ols":
            error = np.sum((ydata - prediction) ** 2)

        if error < min_error:
            min_error = error
            best_T = T

        if min_error < target_error:
            break

    residuals = np.abs(ydata - func(xdata, best_T)) / yerrordata
    stdev_error = np.std(residuals)
    ci_error = 1.96 * stdev_error / np.sqrt(len(xdata))

    return best_T, ci_error
