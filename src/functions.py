import numpy as np

c = 29979245800  # cm s-1
h = 6.62607015e-27  # erg Hz-1
kB = 1.380649e-16  # erg K-1


def planck(nu, T):  # use miu and y parameters too?
    equation = (
        2 * h * c**2 * nu**3 / (np.exp(h * c * nu / (kB * T)) - 1) / c
    )  # unit: erg s−1 sr−1 cm−2 Hz−1

    in_Jy = 1e23 * equation  # unit: Jy
    in_MJy = in_Jy * 1e-6  # unit: MJy

    return in_MJy
