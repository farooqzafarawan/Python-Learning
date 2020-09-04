import tkinter as tk
from tkinter.filedialog import askopenfilename


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
fr_buttons.pack()

btn_open = tk.Button(fr_buttons, text="Scan Drive",
                     width=50, height=60, command=open_file)
btn_save = tk.Button(fr_buttons, text="Format Drive", width=50, height=60)

btn_open.pack(side="left")
btn_save.pack(side="right")

window.mainloop()
