import tkinter as tk
from PIL import ImageTk, Image

homeImage   = r'D:\CODE\images\homeButton.png' 
powerImage  = r'D:\CODE\images\power-button.jpg'
scanImage   = r'D:\CODE\images\usb-4gb.jpg'
formatImage = r'D:\CODE\images\formatUSB-button.jpg'

win = tk.Tk()
width_value = win.winfo_screenwidth()
height_value = win.winfo_screenheight()
win.geometry(f"{width_value}x{height_value}+0+0")
win.resizable(False, True)
win.title("Test GUI")

#win.grid_columnconfigure(0, weight=1)
#win.grid_columnconfigure(1, weight=1)
win.rowconfigure(3, minsize=250, weight=1)
win.columnconfigure([0, 1], minsize=50, weight=1)

# Three frames for icons
topLeftFrame = tk.Frame(win, relief='solid', bd=0)
topLeftFrame.grid(row=0, column=0, padx=10, sticky="w")

middleFrame = tk.Frame( win, relief='solid', bd=0)
middleFrame.grid(row=1, column=0, padx=0, pady=0, sticky="w")

bottomFrame = tk.Frame( win, relief='solid', bd=0)
bottomFrame.grid(row=2, padx=0, pady=0, sticky="sw")


# Top Row Buttons => Home and Power buttons
homeImg = ImageTk.PhotoImage(Image.open(homeImage) )
homeb = tk.Button(topLeftFrame, image=homeImg, height=100, width=100)
homeb.grid(row=0, column=0, padx=10, pady=10)

powerImg = ImageTk.PhotoImage(Image.open(powerImage) )
powerb = tk.Button(topLeftFrame, image=powerImg, height=100, width=100)
powerb.grid(row=0, column=1, padx=10, pady=10)

# Second Row Buttons Scan and Format
scanImg = ImageTk.PhotoImage(Image.open(scanImage) )
scanb = tk.Button(middleFrame, image=scanImg, height=400, width=200)
scanb.grid(row=1, column=0, padx=0, pady=0)

formatImg = ImageTk.PhotoImage(Image.open(formatImage) )
formatb = tk.Button(middleFrame, image=formatImg, height=400, width=200)
formatb.grid(row=1, column=1, padx=0, pady=0)

# Last Row with Label to display result output
lbl_result = tk.Label()
lbl_result.grid(row=2, column=0)

win.mainloop()