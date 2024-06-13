# gui.py
import tkinter as tk
from tkinter import filedialog, Text, Entry, Button, PhotoImage, Frame, Checkbutton, BooleanVar
from pathlib import Path
from main import add_mapping, start_organizing, additional_mappings

def select_directory(entry_2):
    directory = filedialog.askdirectory()
    if directory:
        entry_2.delete(0, tk.END)
        entry_2.insert(0, directory)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sérgio\Desktop\New folder\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = tk.Tk()
window.geometry("500x800")
window.configure(bg="#576F72")

canvas = tk.Canvas(
    window,
    bg="#576F72",
    height=800,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(249.5, 545.5, image=entry_image_1)
entry_1 = Text(bd=0, bg="#E4DCCF", fg="#000716", highlightthickness=0)
entry_1.place(x=47.0, y=422.0, width=405.0, height=245.0)

canvas.create_text(
    112.0, 35.0, anchor="nw", text="Desktop Cleaner", fill="#9cc0b9", font=("Inter Black", 32 * -1)
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(261.0, 128.5, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#F0EBE3", fg="#000716", highlightthickness=0)
entry_2.place(x=126.0, y=117.0, width=270.0, height=21.0)

canvas.create_text(
    7.0, 119.0, anchor="nw", text="Select Directory:", fill="#FFFFFF", font=("Inter Medium", 14 * -1)
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(152.0, 381.5, image=entry_image_3)
entry_3 = Entry(bd=0, bg="#F0EBE3", fg="#000716", highlightthickness=0)
entry_3.place(x=116.0, y=370.0, width=72.0, height=21.0)

canvas.create_text(
    10.0, 372.0, anchor="nw", text="File Extension:", fill="#FFFFFF", font=("Inter Medium", 14 * -1)
)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(331.0, 381.5, image=entry_image_4)
entry_4 = Entry(bd=0, bg="#F0EBE3", fg="#000716", highlightthickness=0)
entry_4.place(x=295.0, y=370.0, width=72.0, height=21.0)

canvas.create_text(
    198.0, 372.0, anchor="nw", text="Folder Name:", fill="#FFFFFF", font=("Inter Medium", 14 * -1)
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: select_directory(entry_2), relief="flat"
)
button_1.place(x=406.0, y=116.0, width=86.0, height=25.371322631835938)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: add_mapping(entry_3.get().strip(), entry_4.get().strip(), entry_1, entry_3, entry_4), relief="flat"
)
button_2.place(x=379.0, y=361.0, width=118.0, height=45.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3, borderwidth=0, highlightthickness=0, command=lambda: start_organizing(entry_2.get().strip(), extension_vars, additional_mappings, entry_2), relief="flat"
)
button_3.place(x=152.0, y=689.0, width=196.0, height=64.0)

canvas.create_rectangle(
    19.0, 81.0, 479.9999470683251, 83.03370777413977, fill="#9cc0b9", outline=""
)

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
    '.mp4': 'AudioAndVideoFiles',
    '.mp3': 'AudioAndVideoFiles',
}

frame_checkboxes = Frame(window, bg="#576F72")
frame_checkboxes.place(x=30, y=170)

extension_vars = {}
row, column = 1, 1
for ext, folder in predefined_extensions.items():
    var = BooleanVar(value=True)  # Set the value to True to check the checkbox by default
    chk = Checkbutton(frame_checkboxes, text=f"{ext}-> {folder}", bg="#576F72", variable=var)
    chk.grid(row=row, column=column, sticky=tk.W, padx=5, pady=2)
    extension_vars[ext] = var
    
    row += 1
    if row == 7:  # Change number of columns here if needed
        row = 1
        column += 1

window.resizable(False, False)
window.mainloop()
