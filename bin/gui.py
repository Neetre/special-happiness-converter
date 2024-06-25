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
        
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_file)
        self.convert_button.pack()

    def browse_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if file_path:
            self.input_path.set(file_path)
            
    def convert_file(self):
        input_file = self.input_path.get()
        output_format = self.output_format.get()

        if not input_file:
            messagebox.showerror("Error", "Please select a file.")
            return

        try:
            if output_format == "mp4":
                self.convert_to_mp4(input_file)
            elif output_format == "mp3":
                self.convert_to_mp3(input_file)
            elif output_format == "png":
                self.convert_to_png(input_file)
            messagebox.showinfo("Success", "Conversion completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
            
    def convert_to_mp4(self, input_file):
        output_file = str(Path(input_file).with_suffix('.mp4'))
        clip = VideoFileClip(input_file)
        clip.write_videofile(output_file)
    
    def convert_to_mp3(self, input_file):
        output_file = str(Path(input_file).with_suffix('.mp3'))
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="mp3")

    def convert_to_png(self, input_file):
        output_file = str(Path(input_file).with_suffix('.png'))
        image = Image.open(input_file)
        image.save(output_file)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()