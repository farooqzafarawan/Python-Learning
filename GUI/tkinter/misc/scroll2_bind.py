import tkinter as tk
from tkinter import ttk
import subprocess

root = tk.Tk()
outWIN = ttk.Frame(root)

canvas = tk.Canvas(outWIN)
scrollbar = ttk.Scrollbar(outWIN, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

output = subprocess.run(["powershell", "ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = output.stdout.decode("utf-8")
output = output.strip('\r')
lstOutput = output.split('\n')

for i in lstOutput:
    ttk.Label(scrollable_frame, text=i).pack()

outWIN.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()