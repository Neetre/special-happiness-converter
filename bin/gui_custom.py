'''
The program creates a GUI for the file converter.
The user can select a file and choose the output format (video, audio, or image) to convert the file to.

Neetre 2024
'''

import customtkinter
from tkinter import filedialog, messagebox
from converter import convert_audio, convert_image, convert_video


video_extensions = ['mp4', 'avi', 'mov', 'mkv']
audio_extensions = ['mp3', 'wav', 'flac']
image_extensions = ['png', 'jpg', 'jpeg', 'heic']


class FileConverterApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("File Converter")
        self.geometry("500x300")
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")

        self.grid_rowconfigure(0, weight=1)  # Make the row expandable
        self.grid_columnconfigure(1, weight=1) 

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.input_label = customtkinter.CTkLabel(master=self.frame, text="Select File:")
        self.input_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.input_path = customtkinter.StringVar()
        self.input_entry = customtkinter.CTkEntry(master=self.frame, textvariable=self.input_path, width=300)
        self.input_entry.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.input_button = customtkinter.CTkButton(master=self.frame, text="Browse", command=self.browse_input)
        self.input_button.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.output_label = customtkinter.CTkLabel(master=self.frame, text="Convert to:")
        self.output_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.type_format = customtkinter.StringVar(value="image")  # default output format
        self.type_options = ["video", "audio", "image"]
        self.type_menu = customtkinter.CTkOptionMenu(master=self.frame, variable=self.type_format, values=self.type_options)
        self.type_menu.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.output_format = customtkinter.StringVar()
        self.output_options = []
        self.output_menu = customtkinter.CTkOptionMenu(master=self.frame, variable=self.output_format, values=self.output_options)

        self.type_format.trace_add("write", self.update_output_menu)
        self.update_output_menu()

        self.output_menu.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.convert_button = customtkinter.CTkButton(master=self.frame, text="Convert", command=self.convert_file)
        self.convert_button.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.progress = customtkinter.CTkProgressBar(master=self.frame, orientation="horizontal", mode='determinate')
        self.progress.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.progress.set(0)
        
    def browse_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if file_path:
            self.input_path.set(file_path)

    def set_menu(self, type_format):
        if type_format == "video":
            base = video_extensions[0]
            return base, video_extensions
        elif type_format == "audio":
            base = audio_extensions[0]
            return base, audio_extensions
        elif type_format == "image":
            base = image_extensions[0]
            return base, image_extensions
        else:
            return "", []

    def update_output_menu(self, *args):
        # Retrieve the new type and update the menu options based on it
        new_type = self.type_format.get()
        output_options = self.set_menu(new_type)
        
        # Update the default value and options for the output format
        self.output_format.set(output_options[0])
        self.output_options = output_options[1]
        
        # Update the options in the output_menu widget
        self.output_menu.configure(values=self.output_options)

            
    def convert_file(self):
        input_file = self.input_path.get()
        output_format = self.output_format.get()
        print(input_file, output_format)

        if not input_file:
            messagebox.showerror("Error", "Please select a file.")
            return

        try:
            if output_format in video_extensions:
                convert_video(input_file, suffix=output_format, progress_bar=self.update_progress)
            elif output_format in audio_extensions:
                convert_audio(input_file, suffix=output_format, progress_bar=self.update_progress)
                self.progress.set(1.0)
            elif output_format in image_extensions:
                convert_image(input_file, suffix=output_format)
                self.progress.set(1.0)

            messagebox.showinfo("Success", "Conversion completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
        finally:
            self.progress.set(0)
        
    def update_progress(self, progress):
        self.progress.set(progress)

def gui_():
    app = FileConverterApp()
    app.mainloop()

if __name__ == "__main__":
    gui_()