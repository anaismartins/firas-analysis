import numpy as np

data = []

# reading data file and parsing it into a numpy matrix
with open("../data/firas_monopole_spec_v1.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line[0] != "#":
            temp = line.split()
            data.append(temp)

data = np.array(data, dtype=float)

# Column 1 = frequency from Table 4 of Fixsen et al., units = cm^-1
# Column 2 = FIRAS monopole spectrum computed as the sum
#             of a 2.725 K BB spectrum and the
#             residual in column 3, units = MJy/sr
# Column 3 = residual monopole spectrum from Table 4 of Fixsen et al.,
#             units = kJy/sr
# Column 4 = spectrum uncertainty (1-sigma) from Table 4 of Fixsen et al.,
#             units = kJy/sr
# Column 5 = modeled Galaxy spectrum at the Galactic poles from Table 4 of
#             Fixsen et al., units = kJy/sr

print(data)
