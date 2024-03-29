import warnings

import matplotlib.pyplot as plt
import numpy as np

from choosing_methods import (
    choose_main_method,
    choose_minimizing_method,
    choose_sampling_method,
)
from functions import planck
from own_algorithm import fit as own_fit
from using_scipy import fit as scipy_fit

# suppress warnings
warnings.filterwarnings("ignore")

red = "#B60000"
blue = "#3E31D6"

method = choose_main_method()
if method == "own" or method == "both":
    sampling_method = choose_sampling_method()
    minimizing_method = choose_minimizing_method()

if method == "scipy":
    filename = f"{method}"
elif method == "own" or method == "both":
    filename = f"{method}_{sampling_method}_{minimizing_method}"

text = "\nEstimate for temperature of CMB assuming it is a black body given by Planck's law with corresponding error with 95% condifence level\n\n"
with open(f"../output/{filename}.txt", "w") as f:
    f.write(text + "\n\n")
print(text)

data = []

# reading data file and parsing it into a numpy matrix
with open("../data/firas_monopole_spec_v1.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line[0] != "#":
            temp = line.split()
            data.append(temp)

data = np.array(data, dtype=float)

# column 1: frequency in cm-1
# column 2: FIRAS monopole spectrum in MJy/sr
# column 2: residual of monopole spectrum in kJy/sr
# column 3: 1 sigma uncertainty
# column 4: modeled galaxy spectrum in kJy/sr

xdata = data[:, 0]
ydata = data[:, 1]
yerrordata = data[:, 3]

plt.errorbar(
    xdata,
    ydata,
    yerrordata,
    fmt=".",
    markersize=5,
    elinewidth=1,
    color=red,
    label="data",
)
plt.xlabel("Frequency (cm-1)")
plt.ylabel("FIRAS Molopole Spectrum (kJy/sr)")


if method == "own" or method == "both":
    own_pred, own_error = own_fit(
        planck,
        xdata,
        ydata,
        yerrordata,
        min=0,
        max=100,
        sampling_method=sampling_method,
        minimizing_method=minimizing_method,
        target_error=0.1,
        max_iterations=1000,
    )
    text = f"Estimate using own algorithm: {own_pred:.5f} +- {own_error:.5f} K"

    print(text)
    with open(f"../output/{filename}.txt", "w") as f:
        f.write(text + "\n")

    # shaded area for the error
    plt.fill_between(
        x=xdata,
        y1=planck(xdata, own_pred - own_error),
        y2=planck(xdata, own_pred + own_error),
        alpha=0.5,
        color=blue,
    )

if method == "scipy" or method == "both":
    scipy_pred, scipy_error = scipy_fit(planck, xdata, ydata, yerrordata)
    text = f"Estimate using scipy built-in function: {scipy_pred:.5f} +- {scipy_error:.5f} K"
    print(text)
    with open(f"../output/{filename}.txt", "a") as f:
        f.write(text)

    # shaded area for the error
    plt.fill_between(
        x=xdata,
        y1=planck(xdata, scipy_pred - scipy_error),
        y2=planck(xdata, scipy_pred + scipy_error),
        alpha=0.5,
        color="black",
    )
    plt.plot(
        xdata,
        planck(xdata, scipy_pred),
        label=f"scipy fit: T = {scipy_pred:.5f} +- {scipy_error:.5f} K",
        color="black",
    )

# to make sure the line is plotted on top of both the shaded areas
if method == "own" or method == "both":
    plt.plot(
        xdata,
        planck(xdata, own_pred),
        label=f"own fit: T = {own_pred:.5f} +- {own_error:.5f} K",
        color=blue,
    )

plt.legend(loc="best")
plt.savefig(f"../output/{filename}.png")
print(f"Plot saved as {filename}.png in output folder")
plt.show()
