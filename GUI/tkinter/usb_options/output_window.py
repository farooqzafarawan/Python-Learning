import sys
import tkinter as tk
import tkinter.ttk as ttk
import subprocess

def createNewWindow():
    output = subprocess.run(["powershell", "ls"], stdout=subprocess.PIPE
                                    , stderr=subprocess.PIPE)
    output = output.stdout.decode("utf-8")
    
    outWindow = tk.Toplevel(app)
    labelExample = tk.Label(outWindow, text = "Output Box")
    
    text = tk.Text(outWindow)
    text.pack()
    text.insert(tk.END, output)

    labelExample.pack()
    buttonExample.pack()

app = tk.Tk()
buttonExample = tk.Button(app,  text="Click to display ls output",  command=createNewWindow)
buttonExample.pack()

app.mainloop()