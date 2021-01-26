#! /usr/bin/env python
#  -*- coding: utf-8 -*-
import sys
import os
import tkinter as tk
import tkinter.ttk as ttk
import subprocess

py3 = True

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
font10 = "-family {Segoe UI} -size 14"
font9 = "-family {Segoe UI} -size 14 -weight bold"

#import usbshield2_support
prog_location = r'D:\script\Python-Learning\GUI\tkinter\usbshield_fateh'
root = tk.Tk()

def shutDown():
    #os.system('shutdown -h now')
    subprocess.call(["shutdown", "-h", "now"])


def outputScan():
    outWIN = tk.Toplevel(root)
    
    outWIN.geometry("600x380+561+251")
    outWIN.minsize(120, 1)
    outWIN.maxsize(1924, 1181)
    outWIN.resizable(1, 1)
    outWIN.title("USBShield-Scanning")
    outWIN.configure(background="#d9d9d9")

    menubar = tk.Menu(outWIN,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
    outWIN.configure(menu = menubar)

    scrollable_frame = tk.Frame(outWIN)
    scrollable_frame.place(relx=0.008, rely=0.016, relheight=0.961, relwidth=0.98)

    scrollable_frame.configure(relief='groove')
    scrollable_frame.configure(borderwidth="2")
    scrollable_frame.configure(relief="groove")
    scrollable_frame.configure(background="#103e04")
    scrollable_frame.configure(highlightbackground="#d9d9d9")
    scrollable_frame.configure(highlightcolor="black")

    Text1 = tk.Text(scrollable_frame)
    Text1.place(relx=0.014, rely=0.142, relheight=0.83, relwidth=0.971)
    Text1.configure(background="#c2e4e1")
    Text1.configure(font="-family {Segoe UI} -size 14")
    Text1.configure(foreground="#103e04")
    Text1.configure(highlightbackground="#d9d9d9")
    Text1.configure(highlightcolor="black")
    Text1.configure(insertbackground="black")
    Text1.configure(padx="5")
    Text1.configure(pady="5")
    Text1.configure(selectbackground="blue")
    Text1.configure(selectforeground="white")
    Text1.configure(wrap="word")

    Label1 = tk.Label(scrollable_frame)
    Label1.place(relx=0.034, rely=0.027, height=35, width=496)
    Label1.configure(activebackground="#f9f9f9")
    Label1.configure(activeforeground="black")
    Label1.configure(background="#c2e4e1")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
    Label1.configure(foreground="#ff0000")
    Label1.configure(highlightbackground="#d9d9d9")
    Label1.configure(highlightcolor="black")
    Label1.configure(text='''Secure-Erasing is in process... Close when completes!''')

    Button_back = tk.Button(scrollable_frame)
    Button_back.place(relx=0.901, rely=0.027, height=34, width=47)
    Button_back.configure(activebackground="#ececec")
    Button_back.configure(activeforeground="#000000")
    Button_back.configure(background="#c2e4e1")
    Button_back.configure(disabledforeground="#a3a3a3")
    Button_back.configure(font=font9)
    Button_back.configure(foreground="#000000")
    Button_back.configure(highlightbackground="#d9d9d9")
    Button_back.configure(highlightcolor="black")
    Button_back.configure(pady="0")
    Button_back.configure(text='''BACK''')
    Button_back.configure(command=outWIN.destroy)

    # Assign output of command to Text widget
    output = subprocess.run(["powershell", "ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = output.stdout.decode("utf-8")
    
    Text1.insert(tk.END, output)

def outputFormat():
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
    closeButton.configure(command=outWIN.destroy)

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


def vp_start_gui(): 
    
        root.geometry("800x480+453+226")
        root.minsize(120, 1)
        root.maxsize(1924, 1181)
        root.resizable(1, 1)
        root.title("USBShield")
        root.configure(background="#103e04")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = menubar)

        scrollable_frame = tk.Frame(root)
        scrollable_frame.place(relx=0.013, rely=0.021, relheight=0.958 , relwidth=0.981)
        scrollable_frame.configure(relief='groove')
        scrollable_frame.configure(borderwidth="2")
        scrollable_frame.configure(relief="groove")
        scrollable_frame.configure(background="#103e04")
        scrollable_frame.configure(highlightbackground="#d9d9d9")
        scrollable_frame.configure(highlightcolor="black")
		
        Button_erase = tk.Button(scrollable_frame)
        Button_erase.place(relx=0.127, rely=0.348, height=135, width=263)
        Button_erase.configure(activebackground="#ececec")
        Button_erase.configure(activeforeground="#000000")
        Button_erase.configure(background="#103e04")
        Button_erase.configure(disabledforeground="#a3a3a3")
        Button_erase.configure(font="-family {Segoe UI} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
        Button_erase.configure(foreground="#103e04")
        Button_erase.configure(highlightbackground="#103e04")
        Button_erase.configure(highlightcolor="#000000")
        photo_location = os.path.join(prog_location,"button_erase.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        Button_erase.configure(image=_img0)
        Button_erase.configure(overrelief="flat")
        Button_erase.configure(pady="0")
        Button_erase.configure(relief="flat")
        Button_erase.configure(text='''Secure Erase / Wipe the USB''')
        Button_erase.configure(command=outputFormat)
		
        Button_scan = tk.Button(scrollable_frame)
        Button_scan.place(relx=0.548, rely=0.348, height=135, width=263)
        Button_scan.configure(activebackground="#ececec")
        Button_scan.configure(activeforeground="#000000")
        Button_scan.configure(background="#103e04")
        Button_scan.configure(disabledforeground="#a3a3a3")
        Button_scan.configure(font="-family {Segoe UI} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
        Button_scan.configure(foreground="#103e04")
        Button_scan.configure(highlightbackground="#103e04")
        Button_scan.configure(highlightcolor="#000000")
        photo_location = os.path.join(prog_location,"button_scan.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        Button_scan.configure(image=_img1)
        Button_scan.configure(overrelief="flat")
        Button_scan.configure(pady="0")
        Button_scan.configure(relief="flat")
        Button_scan.configure(text='''Scan & Clean the USB''')
		
        Label_logo = tk.Label(scrollable_frame)
        Label_logo.place(relx=0.025, rely=0.043, height=90, width=79)
        Label_logo.configure(activebackground="#f9f9f9")
        Label_logo.configure(activeforeground="black")
        Label_logo.configure(background="#103e04")
        Label_logo.configure(disabledforeground="#a3a3a3")
        Label_logo.configure(font="-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0")
        Label_logo.configure(foreground="#103e04")
        Label_logo.configure(highlightbackground="#d9d9d9")
        Label_logo.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"usbshield0.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        Label_logo.configure(image=_img2)
        Label_logo.configure(text='''USBShield Logo''')
		
        Label_below = tk.Label(scrollable_frame)
        Label_below.place(relx=0.127, rely=0.87, height=55, width=574)
        Label_below.configure(activebackground="#f9f9f9")
        Label_below.configure(activeforeground="black")
        Label_below.configure(background="#103e04")
        Label_below.configure(disabledforeground="#a3a3a3")
        Label_below.configure(font=font9)
        Label_below.configure(foreground="#c1edf0")
        Label_below.configure(highlightbackground="#d9d9d9")
        Label_below.configure(highlightcolor="black")
        Label_below.configure(text='''USBShield is mutually developed by Lunesys & SCO
					www.lunesys.com   |   info@lunesys.com   |   Islamabad, Pakistan''')
		
        Button_shutdown = tk.Button(scrollable_frame)
        Button_shutdown.place(relx=0.93, rely=0.043, height=38, width=38)
        Button_shutdown.configure(activebackground="#ececec")
        Button_shutdown.configure(activeforeground="#000000")
        Button_shutdown.configure(background="#103e04")
        Button_shutdown.configure(disabledforeground="#a3a3a3")
        Button_shutdown.configure(foreground="#103e04")
        Button_shutdown.configure(highlightbackground="#103e04")
        Button_shutdown.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"shut.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        Button_shutdown.configure(image=_img3)
        Button_shutdown.configure(overrelief="flat")
        Button_shutdown.configure(pady="0")
        Button_shutdown.configure(relief="flat")
        Button_shutdown.configure(text='''Shutdown''')
		
        Label1_lunesys = tk.Label(scrollable_frame)
        Label1_lunesys.place(relx=0.038, rely=0.891, height=35, width=79)
        Label1_lunesys.configure(activebackground="#f9f9f9")
        Label1_lunesys.configure(activeforeground="black")
        Label1_lunesys.configure(background="#103e04")
        Label1_lunesys.configure(disabledforeground="#a3a3a3")
        Label1_lunesys.configure(foreground="#000000")
        Label1_lunesys.configure(highlightbackground="#d9d9d9")
        Label1_lunesys.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"lunesys.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        Label1_lunesys.configure(image=_img4)
        Label1_lunesys.configure(text='''Lunesys''')
		
        Label1_sco = tk.Label(scrollable_frame)
        Label1_sco.place(relx=0.866, rely=0.891, height=35, width=79)
        Label1_sco.configure(activebackground="#f9f9f9")
        Label1_sco.configure(activeforeground="black")
        Label1_sco.configure(background="#103e04")
        Label1_sco.configure(disabledforeground="#a3a3a3")
        Label1_sco.configure(foreground="#000000")
        Label1_sco.configure(highlightbackground="#d9d9d9")
        Label1_sco.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"sco-logo.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        Label1_sco.configure(image=_img5)
        Label1_sco.configure(text='''SCO''')
		
        Button_info = tk.Button(scrollable_frame)
        Button_info.place(relx=0.866, rely=0.043, height=38, width=38)
        Button_info.configure(activebackground="#ececec")
        Button_info.configure(activeforeground="#000000")
        Button_info.configure(background="#103e04")
        Button_info.configure(disabledforeground="#a3a3a3")
        Button_info.configure(foreground="#103e04")
        Button_info.configure(highlightbackground="#103e04")
        Button_info.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"info.png")
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        Button_info.configure(image=_img6)
        Button_info.configure(overrelief="flat")
        Button_info.configure(pady="0")
        Button_info.configure(relief="flat")
        Button_info.configure(text='''Info''')

if __name__ == '__main__':
    vp_start_gui()
    root.mainloop()

