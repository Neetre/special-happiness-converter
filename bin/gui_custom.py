

import customtkinter
from tkinter import filedialog, messagebox
from pathlib import Path
from converter import convert_audio, convert_image, convert_video


video_extensions = ['mp4', 'avi', 'mov', 'mkv']
audio_extensions = ['mp3', 'wav', 'flac']
image_extensions = ['png', 'jpg', 'jpeg', 'heic']





class FileConverterApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("File Converter")
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.input_label = customtkinter.CTkLabel(master=self.frame, text="Select File:")
        self.input_label.pack(pady=10)
        self.input_path = customtkinter.StringVar()
        self.input_entry = customtkinter.CTkEntry(master=self.frame, textvariable=self.input_path, width=300)
        self.input_entry.pack(pady=10)
        self.input_button = customtkinter.CTkButton(master=self.frame, text="Browse", command=self.browse_input)
        self.input_button.pack(pady=10)

        self.output_label = customtkinter.CTkLabel(master=self.frame, text="Convert to:")
        self.output_label.pack(pady=10)

        self.type_format = customtkinter.StringVar(value="mp4")  # default output format
        self.type_options = ["mp4", "mp3", "png"]
        self.type_menu = customtkinter.CTkOptionMenu(master=self.frame, variable=self.type_format, values=self.type_options)
        self.output_menu.pack(pady=10)

        self.output_format = customtkinter.StringVar(value="mp4")  # default output format
        self.output_options = ["mp4", "mp3", "png"]
        self.output_menu = customtkinter.CTkOptionMenu(master=self.frame, variable=self.output_format, values=self.output_options)
        self.output_menu.pack(pady=10)
        
        self.convert_button = customtkinter.CTkButton(master=self.frame, text="Convert", command=self.convert_file)
        self.convert_button.pack(pady=20)

        self.progress = customtkinter.CTkProgressBar(master=self.frame, mode='determinate')
        self.progress.pack(pady=20, fill='x')
        
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
                self.progress.set(1.0)
            elif output_format in image_extensions:
                convert_image(input_file, suffix=".png")
                self.progress.set(1.0)

            messagebox.showinfo("Success", "Conversion completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
        finally:
            self.progress.set(0)
        
    def update_progress(self, progress):
        self.progress.set(progress)

def gui():
    app = FileConverterApp()
    app.mainloop()

if __name__ == "__main__":
    gui()