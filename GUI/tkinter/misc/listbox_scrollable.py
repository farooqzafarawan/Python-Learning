import tkinter as tk
import tkinter.ttk as ttk
import subprocess


#root = tk.Tk()
outWIN = tk.Tk()

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'

outWIN.geometry("600x380+561+251")
outWIN.minsize(120, 1)
outWIN.maxsize(1924, 1181)
outWIN.resizable(1, 1)
outWIN.title("USBShield-Erasing")
outWIN.configure(background="#d9d9d9")

menubar = tk.Menu(outWIN,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
outWIN.configure(menu = menubar)

Frame1 = tk.Frame(outWIN)
Frame1.place(relx=0.008, rely=0.016, relheight=0.961, relwidth=0.98)

Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#103e04")
Frame1.configure(highlightbackground="#d9d9d9")
Frame1.configure(highlightcolor="black")

canvasOut = tk.Canvas(Frame1)

#Adding scrollbar
scbar = tk.Scrollbar(Frame1)

Entry_output = tk.Label(canvasOut)
Entry_output.place(relx=0.014, rely=0.142, relheight=0.83, relwidth=0.971)
Entry_output.configure(background="#c2e4e1")
Entry_output.configure(font="-family {Segoe UI} -size 14")
Entry_output.configure(foreground="#103e04")
Entry_output.configure(highlightbackground="#d9d9d9")
Entry_output.configure(highlightcolor="black")

#Entry_output.configure(yscrollcommand=scbar.set)

scbar.pack(side=tk.RIGHT, fill=tk.Y)
canvasOut.configure(yscrollcommand=scbar.set)


#scbar.pack(side=tk.RIGHT, fill=tk.Y)
Entry_output.pack(side=tk.LEFT)

# Assign output of command to Text widget
output = subprocess.run(["powershell", "ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = output.stdout.decode("utf-8")
# output = output.strip('\r')
# lstOutput = output.split('\n')


Entry_output['text'] = output

outWIN.mainloop()