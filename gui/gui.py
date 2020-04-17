"""
TODO:
- write a README in github repo with idiot proof instructions
- return to mainloop when load data is cancelled without asking for save data
- dropdown menu for convert to file endings
- convert all files of a directory to chosen format: https://stackoverflow.com/questions/42438380/ffmpeg-in-python-script
- only open terminal window or error window in case of error (for debugging)
- show progress bar with name of file to be converted
- why the slow startup?
- create a publicly accessible doc on github for error reporting and feature suggestions
- add icons to executables

how to make executables with pyinstaller

on Mac: pyinstaller
--onefile
--windowed
--icon=icons/mac.png
--add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk'
--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl'
GUI.py

on Windows:
pyinstaller --onefile --add-binary="dependencies\windows\ffmpeg.exe;." GUI.py
"""

import tkinter as tk
from tkinter import filedialog as fd
import os
import sys


class GUI:
    """ Initialization """

    def set_variables(self):
        self.gui_height = 100
        self.gui_width = 200
        self.set_path_to_ffmpeg()

    def set_path_to_ffmpeg(self):
        try:
            self.convert_ffmpeg_path = os.path.join(sys._MEIPASS, "ffmpeg.exe")
        except AttributeError:
            self.convert_ffmpeg_path = os.path.join(
                os.path.abspath("."), r"dependencies\windows\ffmpeg.exe"
            )

    def define_gui_elements(self):
        self.root.title("File Converter")
        self.canvas = tk.Canvas(self.root, height=self.gui_height, width=self.gui_width)
        self.frame = tk.Frame(self.root)
        self.convert_button = tk.Button(
            self.frame, text="Convert file", command=self.convert_file
        )

    """ Main program elements """

    def load_file(self):
        self.load_filename = fd.askopenfilename()

    def save_file(self):
        self.save_filename = fd.asksaveasfilename()

    def convert_file(self):
        self.load_file()
        self.save_file()
        self.convert_flag = f" -i {self.load_filename} {self.save_filename}"
        self.convert_command = self.convert_ffmpeg_path + self.convert_flag
        print(self.convert_command)
        os.system(self.convert_command)

    def activate_gui_elements(self):
        self.canvas.pack()
        self.frame.place(relwidth=1, relheight=1)
        self.convert_button.place(relx=0.5, rely=0.5, anchor="center")

    """Execution as script"""

    def main(self):
        self.set_variables()
        self.run()

    def run(self):
        self.root = tk.Tk()
        self.define_gui_elements()
        self.activate_gui_elements()
        self.root.mainloop()


if __name__ == "__main__":
    program = GUI()
    program.main()