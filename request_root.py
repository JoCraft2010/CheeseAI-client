import os
from elevate import elevate
import PySimpleGUI


def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return False


def request_root():
    if not is_admin():
        try:
            elevate(show_console=False)
        except OSError:
            PySimpleGUI.popup_ok("Couldn't obtain root privileges. Root\nprivileges are recommended for better\n"
                                 "performance & storage optimizations.")
