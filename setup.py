import sys


def setup_win():
    print("WARNING: Only Windows setup supported yet.")
    if len(sys.argv) < 2:
        print("No arguments were provided. Please run \"python prepare_setup.py\" first.")
        return
    flags = sys.argv[2:]
    use_CUDA = False
    if sys.argv[1] == "cu121":
        print("Please execute \"./dependencies_setup/install_cu121.ps1\" in PowerShell.")
        use_CUDA = True
    elif sys.argv[1] == "cu118":
        print("Please execute \"./dependencies_setup/install_cu118.ps1\" in PowerShell.")
        use_CUDA = True
    elif sys.argv[1] == "cpu":
        print("Please execute \"./dependencies_setup/install_cpu.ps1\" in PowerShell.")
    else:
        print("Processor type " + sys.argv[1] + " isn't supported (yet).")
        return

    config = f"[general]\n" \
             f"use_CUDA: {int(use_CUDA)}\n" \
             f"\n" \
             f"[patches]\n" \
             f"GTX1660_patch: {int('--GTX1660_patch' in flags)}\n"

    with open("config.ini", "w") as f:
        f.write(config)
    print("\nYour CheeseAI client installation is nearly done.")


if __name__ == '__main__':
    setup_win()
    input("Press enter to quit...")
