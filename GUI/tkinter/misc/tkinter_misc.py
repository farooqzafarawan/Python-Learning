import tkinter as tk
from PIL import ImageTk, Image
import os

homeDir  = r"D:\CODE\images"
file1 = "homeButton.png"

#homeImage = os.path.join(homeDir,file1)
homeImage   = r'D:\CODE\images\homeButton.png' 
powerImage  = r'D:\CODE\images\power-button.jpg'
scanImage   = r'D:\CODE\images\power-4gb.jpg'
formatImage = r'D:\CODE\images\formatUSB-button.jpg'

win = tk.Tk()
width_value = win.winfo_screenwidth()
height_value = win.winfo_screenheight()
win.geometry(f"{width_value}x{height_value}+0+0")
win.resizable(False, True)
win.title("USB Options")

win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)

topLeftFrame = tk.Frame(win, relief='flat', width=300, height=200, bd=2)
topLeftFrame.grid(row=0, column=0, padx=10, sticky="w")

# Top Row Buttons => Home and Power buttons
homeImg = ImageTk.PhotoImage(Image.open(homeImage) )
homeb = tk.Button(topLeftFrame, image=homeImg, height=100, width=100)
homeb.grid(row=0, column=0, padx=10, pady=10)

powerImg = ImageTk.PhotoImage(Image.open(powerImage) )
powerb = tk.Button(topLeftFrame, image=powerImg, height=100, width=100)
powerb.grid(row=0, column=1, padx=10, pady=10)

win.mainloop()