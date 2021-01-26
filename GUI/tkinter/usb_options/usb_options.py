import subprocess
import random
import tkinter as tk


def scanVirus():
    try:
        output = subprocess.run(["powershell", "date"], universal_newlines=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    except FileNotFoundError as e:
        print(e)

    lbl_result["text"] = output


window = tk.Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

btn_roll = tk.Button(text="Scan", command=scanVirus)
lbl_result = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

window.mainloop()
