# main.py
import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Initialize additional mappings
additional_mappings = {}

def organize_files(directory, selected_extensions, additional_mappings):
    folders = {
        '.txt': 'TextFiles',
        '.jpg': 'ImageFiles',
        ".jpeg": "ImageFiles",
        ".png": "ImageFiles",
        ".gif": "ImageFiles",
        '.pdf': 'PDFFiles',
        '.docx': 'TextFiles',
        '.xlsx': 'TextFiles',
        '.csv': 'TextFiles',
        '.pptx': 'TextFiles',
        '.rar': 'ZippedFiles',
        '.zip': 'ZippedFiles',
        '.exe': 'Applications',
        '.msi': 'Applications',
        '.java': 'ProgrammingFiles',
        '.html': 'ProgrammingFiles',
        '.php': 'ProgrammingFiles',
        '.mp4': 'AudioAndVideoFiles',
        '.mp3': 'AudioAndVideoFiles',
    }

    filtered_folders = {ext: folder for ext, folder in folders.items() if ext in selected_extensions}
    filtered_folders.update(additional_mappings)

    for folder in filtered_folders.values():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file_extension, folder_name in filtered_folders.items():
        files_to_move = [file for file in os.listdir(directory) if file.endswith(file_extension)]
        for file in files_to_move:
            src = os.path.join(directory, file)
            dest = os.path.join(directory, folder_name, file)
            shutil.move(src, dest)

def add_mapping(extension, folder_name, entry_1, entry_3, entry_4):
    if extension and folder_name:
        additional_mappings[extension] = folder_name
        entry_1.insert(tk.END, f"{extension} -> {folder_name}\n")
        entry_3.delete(0, tk.END)
        entry_4.delete(0, tk.END)

def start_organizing(directory, extension_vars, additional_mappings, entry_2):
    if directory and os.path.isdir(directory):
        selected_extensions = [ext for ext, var in extension_vars.items() if var.get()]
        organize_files(directory, selected_extensions, additional_mappings)
        messagebox.showinfo("Success", "Files have been organized successfully.")
    else:
        messagebox.showerror("Error", "Please select a valid directory.")
