import tkinter as tk
import sys
import os
import signal
import threading
import time


class ConsoleWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CheeseAI client - Console")
        self.output_text = tk.Text(self, height=40, width=160)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.output_text.tag_config("error", foreground="red")
        self.output_text.tag_config("warning", foreground="orange")

    def write(self, message):
        if "ERROR" in message:
            self.output_text.insert(tk.END, message, "error")
        elif "WARNING" in message:
            self.output_text.insert(tk.END, message, "warning")
        else:
            self.output_text.insert(tk.END, message)
        self.output_text.update_idletasks()

    def flush(self):
        pass

    def on_close(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        self.destroy()
        os.kill(os.getpid(), signal.SIGTERM)


def run_gui():
    console_window = ConsoleWindow()
    sys.stdout = console_window
    sys.stderr = console_window
    console_window.mainloop()


def create_gui():
    gui_thread = threading.Thread(target=run_gui)
    gui_thread.start()

    time.sleep(.5)
