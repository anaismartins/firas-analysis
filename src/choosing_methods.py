def choose_main_method():
    possibilities = ["own", "scipy", "both"]

    method = input(
        "Enter the corresponding number of the method for evaluating the temperature of the CMB you want to choose:\n1: own\n2: scipy\n3: both\n"
    )
    if method == "":
        print("No method chosen, defaulting to both")
        method = "both"

    while method not in possibilities:
        try:
            method = int(method)
            method = possibilities[method - 1]
        except ValueError:
            method = input("\nPlease input the corresponding number: ")

    return method


def choose_sampling_method():
    possibilities = ["uniform"]

    sampling_method = input(
        "\nEnter the corresponding number of the sampling method you want to choose:\n1: uniform\n"
    )
    if sampling_method == "":
        print("No method chosen, defaulting to uniform")
        sampling_method = "uniform"

    while sampling_method not in possibilities:
        try:
            sampling_method = int(sampling_method)
            sampling_method = possibilities[sampling_method - 1]
        except ValueError:
            input("\nPlease input the corresponding number: ")

    return sampling_method


def choose_minimizing_method():
    possibilities = ["rms"]

    minimizing_method = input(
        "\nEnter the corresponding number of the minimizing method you want to choose:\n1: rms\n"
    )
    if minimizing_method == "":
        print("\nNo method chosen, defaulting to rms")
        minimizing_method = "rms"

    while minimizing_method not in possibilities:
        try:
            minimizing_method = int(minimizing_method)
            minimizing_method = possibilities[minimizing_method - 1]
        except ValueError:
            input("Please input the corresponding number: ")

    return minimizing_method
