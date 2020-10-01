from tkinter import *
import subprocess

window = Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

def listFiles():
    try:
        output = subprocess.run(["powershell", "ls"], stdout=subprocess.PIPE
                                , stderr=subprocess.PIPE)
        lbl_result["text"] = output.stdout.decode("utf-8")
    except Exception as e:
        print(e)


btn_roll = Button(text="List Files", command=listFiles)
lbl_result = Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

window.mainloop()