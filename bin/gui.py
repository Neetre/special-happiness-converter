'''
Gui for File Converter

Neetre 2024
'''

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar

from converter import convert_audio, convert_image, convert_video

video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
audio_extensions = ['.mp3', '.wav', '.flac']
image_extensions = ['.png', '.jpg', '.jpeg', 'heic']

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Converter")
        self.progress = Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress.pack()

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
            if output_format in video_extensions:
                convert_video(input_file, format="mp4", progress_bar=self.update_progress)
            elif output_format in audio_extensions:
                convert_audio(input_file, format="mp3", progress_bar=self.update_progress)
            elif output_format in image_extensions:
                convert_image(input_file, suffix=".png")
                self.progress['value'] = 100

            messagebox.showinfo("Success", "Conversion completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
        finally:
            self.progress.stop()
        
    def update_progress(self, progress):
        self.progress['value'] = progress


def gui():
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    gui()