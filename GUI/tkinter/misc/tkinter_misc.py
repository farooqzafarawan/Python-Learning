
import tkinter as tk
import subprocess

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'

root = tk.Tk()

outWIN = tk.Toplevel(root)
outWIN.geometry("680x400+543+286")
outWIN.minsize(1, 1)
outWIN.maxsize(1905, 1170)
outWIN.resizable(1, 1)
outWIN.title("USBShield-Erasing")
outWIN.configure(background="#d9d9d9")

menubar = tk.Menu(outWIN,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
outWIN.configure(menu = menubar)

Frame2 = tk.Frame(outWIN)
Frame2.place(relx=0.015, rely=0.025, relheight=0.188, relwidth=0.971)
Frame2.configure(relief='groove')
Frame2.configure(borderwidth="2")
Frame2.configure(relief="groove")

topLabel = tk.Label(Frame2)
topLabel.place(relx=0.015, rely=0.133, height=47, width=391)
topLabel.configure(foreground="#ff0000")
topLabel.configure(text='''ERASING the USB... Close when done!''')

closeButton = tk.Button(Frame2)
closeButton.place(relx=0.833, rely=0.133, height=55, width=97)

closeButton.configure(text='''CLOSE''')

Frame1 = tk.Frame(outWIN)
Frame1.place(relx=0.015, rely=0.225, relheight=0.75, relwidth=0.971)

Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")

canvas1 = tk.Canvas(Frame1)
canvas1.place(relx=0.015, rely=0.033, relheight=0.933, relwidth=0.97)
canvas1.configure(borderwidth="2")
canvas1.configure(relief="ridge")
canvas1.configure(selectbackground="blue")
canvas1.configure(selectforeground="white")

canvasLabel = tk.Label(canvas1)
canvasLabel.place(relx=0.0, rely=0.0, height=280, width=640)
canvasLabel.configure(text='''Label''')
#Scroll Code
#canvas = tk.Canvas(outWIN)
scrollbar = tk.Scrollbar(Frame1, orient="vertical", command=canvas1.yview)
scrollable_frame = tk.Frame(canvas1)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas1.configure( scrollregion=canvas1.bbox("all")    )
)

canvas1.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas1.configure(yscrollcommand=scrollbar.set)

output = subprocess.run(["powershell", "ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = output.stdout.decode("utf-8")
output = output.strip('\r')
lstOutput = output.split('\n')

for i in lstOutput:
    tk.Label(scrollable_frame, text=i).pack()

#outWIN.pack()
canvas1.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()