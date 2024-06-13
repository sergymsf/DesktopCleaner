import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to organize files
def organize_files(directory, selected_extensions, additional_mappings):
    # Dictionary of predefined folders
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

    # Filter the folders dictionary based on selected extensions
    filtered_folders = {ext: folder for ext, folder in folders.items() if ext in selected_extensions}

    # Update the folders dictionary with additional mappings
    filtered_folders.update(additional_mappings)

    # Create folders for each category
    for folder in filtered_folders.values():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files into their corresponding folders
    for file_extension, folder_name in filtered_folders.items():
        files_to_move = [file for file in os.listdir(directory) if file.endswith(file_extension)]
        for file in files_to_move:
            src = os.path.join(directory, file)
            dest = os.path.join(directory, folder_name, file)
            shutil.move(src, dest)

# Function to select a directory
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, directory)

# Function to add additional mappings
def add_mapping():
    extension = entry_extension.get().strip()
    folder_name = entry_folder_name.get().strip()
    if extension and folder_name:
        additional_mappings[extension] = folder_name
        listbox_mappings.insert(tk.END, f"{extension} -> {folder_name}")
        entry_extension.delete(0, tk.END)
        entry_folder_name.delete(0, tk.END)

# Function to start organizing
def start_organizing():
    directory = entry_directory.get().strip()
    if directory and os.path.isdir(directory):
        selected_extensions = [ext for ext, var in extension_vars.items() if var.get()]
        organize_files(directory, selected_extensions, additional_mappings)
        messagebox.showinfo("Success", "Files have been organized successfully.")
    else:
        messagebox.showerror("Error", "Please select a valid directory.")

# Initialize main window
root = tk.Tk()
root.title("File Organizer")

additional_mappings = {}

# Directory selection
frame_directory = tk.Frame(root)
frame_directory.pack(pady=10)
label_directory = tk.Label(frame_directory, text="Directory to clean:")
label_directory.pack(side=tk.LEFT)
entry_directory = tk.Entry(frame_directory, width=50)
entry_directory.pack(side=tk.LEFT, padx=10)
button_browse = tk.Button(frame_directory, text="Browse", command=select_directory)
button_browse.pack(side=tk.LEFT)

# Predefined extension checkboxes
predefined_extensions = {
    '.txt': 'TextFiles',
    '.docx': 'TextFiles',
    '.xlsx': 'TextFiles',
    '.csv': 'TextFiles',
    '.pptx': 'TextFiles',
    '.pdf': 'PDFFiles',
    '.jpg': 'ImageFiles',
    ".jpeg": "ImageFiles",
    ".png": "ImageFiles",
    ".gif": "ImageFiles",
    '.rar': 'ZippedFiles',
    '.zip': 'ZippedFiles',
    '.java': 'ProgrammingFiles',
    '.html': 'ProgrammingFiles',
    '.php': 'ProgrammingFiles',
    '.exe': 'Applications',
    '.msi': 'Applications',
    '.mp4': 'AudioAndVideoFiles',
    '.mp3': 'AudioAndVideoFiles',
}

frame_checkboxes = tk.Frame(root)
frame_checkboxes.pack(pady=10)
label_checkboxes = tk.Label(frame_checkboxes, text="Select extensions to organize:")
label_checkboxes.grid(row=0, column=0, columnspan=4)

extension_vars = {}
row, column = 1, 1
for ext, folder in predefined_extensions.items():
    var = tk.BooleanVar(value=True)  # Set the value to True to check the checkbox by default
    chk = tk.Checkbutton(frame_checkboxes, text=f"{ext} -> {folder}", variable=var)
    chk.grid(row=row, column=column, sticky=tk.W, padx=5, pady=2)
    extension_vars[ext] = var
    
    row += 1
    if row == 6:  # Change number of columns here if needed
        row = 1
        column += 1

# Additional mappings
frame_mappings = tk.Frame(root)
frame_mappings.pack(pady=10)
label_extension = tk.Label(frame_mappings, text="File Extension:")
label_extension.pack(side=tk.LEFT)
entry_extension = tk.Entry(frame_mappings, width=10)
entry_extension.pack(side=tk.LEFT, padx=5)
label_folder_name = tk.Label(frame_mappings, text="Folder Name:")
label_folder_name.pack(side=tk.LEFT)
entry_folder_name = tk.Entry(frame_mappings, width=20)
entry_folder_name.pack(side=tk.LEFT, padx=5)
button_add_mapping = tk.Button(frame_mappings, text="Add Mapping", command=add_mapping)
button_add_mapping.pack(side=tk.LEFT, padx=5)

# List of mappings
frame_listbox = tk.Frame(root)
frame_listbox.pack(pady=10)
listbox_mappings = tk.Listbox(frame_listbox, width=50, height=10)
listbox_mappings.pack(side=tk.LEFT)
scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL, command=listbox_mappings.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
listbox_mappings.config(yscrollcommand=scrollbar.set)

# Start button
button_start = tk.Button(root, text="Start Organizing", command=start_organizing)
button_start.pack(pady=20)

root.mainloop()
