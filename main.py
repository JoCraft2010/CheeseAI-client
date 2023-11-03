import request_root
import gui_console
import webui_manager

if __name__ == "__main__":
    request_root.request_root()
    gui_console.create_gui()
    webui_manager.start()
