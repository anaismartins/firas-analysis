method = "both"
"""
OPTIONS FOR METHOD:
"own" - use algorithm coded by me
"scipy" - use curve_fit function from the scipy library
"both" - use both methods
"""

sampling_method = "uniform"
"""
OPTIONS FOR SAMPLING_METHOD (only useful if choosing "own" or "both" method):
uniform - sample uniformly from the interval [0, 293.15]K - minimum possible temperature and NTP temperature
"""

minimizing_method = "rms"
"""
OPTIONS FOR MINIMIZING_METHOD (only useful if choosing "own" or "both" method):
rms - root mean square error
"""
