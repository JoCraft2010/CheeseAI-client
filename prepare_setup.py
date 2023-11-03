import sys


def _in_venv():
    return sys.prefix != sys.base_prefix


def _ask_yn(question):
    a = input(question + " [Y]es/[N]o: ").lower()
    if a == "y":
        return True
    if a == "n":
        return False
    print("Please give a valid answer.")
    return _ask_yn(question)


def setup():
    print("CheeseAI client installation setup")
    if not _in_venv():
        print("Please put all the source code into a venv with pip installed.")
        return
    use_CUDA = _ask_yn("Do you have an NVIDIA GPU supporting CUDA>=11.8?")
    if use_CUDA:
        print("Using CUDA drivers for GPU computation.")
        use_CUDA_legacy = _ask_yn("Do you want to fall back to CUDA 11.8 (older devices)? CUDA 12.1 will be used instead. (WARNING: CUDA_legacy isn't properly tested.) [CUDA_legacy]")
        use_GTX1660_patch = _ask_yn("Do you have an NVIDIA GeForce GTX 1660? (WARNING: Only GTX1660_patch is properly tested.) [GTX1660_patch]")
        if use_CUDA_legacy:
            CUDA_version = "11.8"
            CUDA_versionC = "118"
        else:
            CUDA_version = "12.1"
            CUDA_versionC = "121"
        if use_GTX1660_patch:
            print("You will use CUDA " + CUDA_version + " [cu" + CUDA_versionC + "] with the GTX 1660 patch [GTX1660_patch].")
            s_code = "py setup.py cu" + CUDA_versionC + " --GTX1660_patch"
        else:
            print("You will use CUDA " + CUDA_version + " [cu" + CUDA_versionC + "] without the GTX 1660 patch [GTX1660_patch].")
            s_code = "py setup.py cu" + CUDA_versionC
        print("To install all dependencies and update all project configurations, please execute the following command inside the venv:\n")
        print(s_code)
    else:
        print("Falling back to CPU.")
        s_code = "py setup.py cpu"
        print("To install all dependencies and update all project configurations, please execute the following command inside the venv:\n")
        print(s_code)
    print("\nYour CheeseAI client installation setup is done.")


if __name__ == '__main__':
    setup()
    input("Press enter to quit...")
