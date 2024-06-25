'''
Gui for File Converter

Neetre 2024
'''

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path



class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Converter")

        self.input_label = tk.Label(root, text="Select File:")
        self.input_label.pack()
        self.input_path = tk.StringVar()
        self.input_entry = tk.Entry(root, textvariable=self.input_path, width=50)
        self.input_entry.pack()
        self.input_button = tk.Button(root, text="Browse", command=self.browse_input)
        self.input_button.pack()

        self.output_label = tk.Label(root, text="Convert to:")
        self.output_label.pack()
        self.output_format = tk.StringVar()
        self.output_format.set("mp4")  # default output format
        self.output_options = ["mp4", "mp3", "png"]
        self.output_menu = tk.OptionMenu(root, self.output_format, *self.output_options)
        self.output_menu.pack()

    def browse_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if file_path:
            self.input_path.set(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()