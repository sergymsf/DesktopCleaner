import os

desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Downloads')
print("Desktop Path:", desktop_path)

files_on_desktop = os.listdir(desktop_path)
with open('desktop_files.txt', 'w', encoding='utf-8') as file:
    file.write("Files on Desktop:\n")
    for file_name in files_on_desktop:
        try:
            file.write(file_name + '\n')
        except UnicodeEncodeError:
            file.write("[Encoding Error: Cannot display filename]\n")

file_extensions = {}

for file_name in files_on_desktop:
    if os.path.isfile(os.path.join(desktop_path, file_name)):
        extension = os.path.splitext(file_name)[1]
        if extension:
            if extension not in file_extensions:
                file_extensions[extension] = []
            file_extensions[extension].append(file_name)

with open('file_extensions.txt', 'w', encoding='utf-8') as file:
    file.write("File Extensions:\n")
    for extension, files in file_extensions.items():
        try:
            file.write(extension + " : " + ", ".join(files) + '\n')
        except UnicodeEncodeError:
            file.write("[Encoding Error: Cannot display filename]\n")

import os
import shutil

desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Downloads')

# Create a dictionary to store file extensions and their corresponding folders
folders = {
    '.txt': 'TextFiles',
    '.jpg': 'ImageFiles',
    ".jpeg": "ImageFiles",  # Add other image file extensions if needed
    ".png": "ImageFiles",
    ".gif": "ImageFiles",
    '.pdf': 'PDFFiles',
    '.docx': 'TextFiles',
    '.xlsx': 'TextFiles',
    '.csv': 'TextFiles',
    '.pptx': 'TextFiles',
    '.rar': 'ZipedFiles',
    '.zip': 'ZipedFiles',
    '.exe': 'Aplications',
    '.msi': 'Aplications',
    '.java': 'ProgramingFiles',
    '.html': 'ProgramingFiles',
    '.php': 'ProgramingFiles',
    '.mp4': 'AudioAndVideoFiles',
    '.mp3': 'AudioAndVideoFiles',
    # Add more file extensions and corresponding folder names as needed
}

# Create folders for each category
for folder in folders.values():
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files into their corresponding folders
for file_extension, folder_name in folders.items():
    files_to_move = [file for file in os.listdir(desktop_path) if file.endswith(file_extension)]
    for file in files_to_move:
        src = os.path.join(desktop_path, file)
        dest = os.path.join(desktop_path, folder_name, file)
        shutil.move(src, dest)

print("Files have been organized on the desktop.")
