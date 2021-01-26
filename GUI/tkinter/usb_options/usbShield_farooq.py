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


def outputWIN():
    outWIN = tk.Toplevel(root)

    outWIN.geometry("600x550+253+226")
    outWIN.minsize(120, 1)
    outWIN.maxsize(800, 600)
    outWIN.resizable(1, 1)
    outWIN.title("USBShield-Erasing")
    outWIN.configure(background="#103e04")
    outWIN.configure(highlightbackground="#d9d9d9")
    outWIN.configure(highlightcolor="black")

    menubar = tk.Menu(outWIN,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
    outWIN.configure(menu = menubar)

    Frame1 = tk.Frame(outWIN)
    Frame1.place(relx=0.01, rely=0.017, relheight=0.958, relwidth=0.991)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#103e04")
    Frame1.configure(highlightbackground="#d9d9d9")
    Frame1.configure(highlightcolor="black")

    Label1 = tk.Label(Frame1)
    Label1.place(relx=0.01, rely=0.035, height=41, relwidth=0.84)
    Label1.configure(background="#c2e4e1")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font=font9)
    Label1.configure(foreground="#ff0000")
    Label1.configure(text='''Secure-Erasing in process. Click BACK when completes''')

    Button_back = tk.Button(Frame1)
    Button_back.place(relx=0.886, rely=0.035, height=80, width=80)
    Button_back.configure(activebackground="#ececec")
    Button_back.configure(activeforeground="#000000")
    Button_back.configure(background="#103e04")
    Button_back.configure(disabledforeground="#a3a3a3")
    Button_back.configure(foreground="#103e04")
    Button_back.configure(highlightbackground="#d9d9d9")
    Button_back.configure(highlightcolor="black")
    photo_location = os.path.join(prog_location,"back.png")

    global _imgBack
    _imgBack = tk.PhotoImage(file=photo_location)
    Button_back.configure(image=_imgBack)
    Button_back.configure(overrelief="flat")
    Button_back.configure(pady="0")
    Button_back.configure(relief="flat")
    Button_back.configure(text='''Back''')
    Button_back.configure(command=outWIN.destroy)
    
    Text1 = tk.Text(Frame1)
    Text1.place(relx=0.0129, rely=0.122, relheight=0.79, relwidth=0.84)
    Text1.configure(background="#c2e4e1")
    Text1.configure(font=font10)
    Text1.configure(foreground="#103e04")
    Text1.configure(highlightbackground="#d9d9d9")
    Text1.configure(highlightcolor="black")
    Text1.configure(insertbackground="black")
    Text1.configure(padx="5")
    Text1.configure(pady="5")
    Text1.configure(selectbackground="blue")
    Text1.configure(selectforeground="white")
    Text1.configure(wrap="word")

    # Assign output of command to Text widget
    output = subprocess.run(["powershell", "ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = output.stdout.decode("utf-8")
    
    Text1.insert(tk.END, output)

def vp_start_gui():
    
    root.geometry("1024x600+453+226")
    root.minsize(120, 1)
    root.maxsize(1924, 1181)
    root.resizable(1, 1)
    root.title("USBShield")
    root.configure(background="#103e04")
    root.configure(highlightbackground="#d9d9d9")
    root.configure(highlightcolor="black")

    menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
    root.configure(menu = menubar)

    Frame1 = tk.Frame(root)
    Frame1.place(relx=0.01, rely=0.017, relheight=0.958, relwidth=0.981)

    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#103e04")
    Frame1.configure(highlightbackground="#d9d9d9")
    Frame1.configure(highlightcolor="black")

    Button_info = tk.Button(Frame1)
    Button_info.place(relx=0.876, rely=0.017, height=50, width=51)
    Button_info.configure(activebackground="#ececec")
    Button_info.configure(activeforeground="#000000")
    Button_info.configure(background="#103e04")
    Button_info.configure(disabledforeground="#a3a3a3")
    Button_info.configure(foreground="#103e04")
    Button_info.configure(highlightbackground="#d9d9d9")
    Button_info.configure(highlightcolor="black")
    photo_location = os.path.join(prog_location,"info.png")

    global _img0
    _img0 = tk.PhotoImage(file=photo_location)
    Button_info.configure(image=_img0)
    Button_info.configure(overrelief="flat")
    Button_info.configure(pady="0")
    Button_info.configure(relief="flat")
    Button_info.configure(text='''Info''')
    Button_info.configure(command=outputWIN) # calling  outputWIN function to display output in new window

    Button_erase = tk.Button(Frame1)
    Button_erase.place(relx=0.1, rely=0.348, height=180, width=350)
    Button_erase.configure(activebackground="#ececec")
    Button_erase.configure(activeforeground="#000000")
    Button_erase.configure(background="#103e04")
    Button_erase.configure(disabledforeground="#a3a3a3")
    Button_erase.configure(font="-family {Segoe UI} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Button_erase.configure(foreground="#103e04")
    Button_erase.configure(highlightbackground="#d9d9d9")
    Button_erase.configure(highlightcolor="#000000")
    photo_location = os.path.join(prog_location,"button_erase.png")

    global _img1
    _img1 = tk.PhotoImage(file=photo_location)
    Button_erase.configure(image=_img1)
    Button_erase.configure(overrelief="flat")
    Button_erase.configure(pady="0")
    Button_erase.configure(relief="flat")
    Button_erase.configure(text='''Secure Erase / Wipe the USB''')

    Button_scan = tk.Button(Frame1)
    Button_scan.place(relx=0.557, rely=0.348, height=180, width=350)
    Button_scan.configure(activebackground="#ececec")
    Button_scan.configure(activeforeground="#000000")
    Button_scan.configure(background="#103e04")
    Button_scan.configure(disabledforeground="#a3a3a3")
    Button_scan.configure(font="-family {Segoe UI} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Button_scan.configure(foreground="#103e04")
    Button_scan.configure(highlightbackground="#103e04")
    Button_scan.configure(highlightcolor="#000000")
    photo_location = os.path.join(prog_location,"button_scan.png")

    global _img2
    _img2 = tk.PhotoImage(file=photo_location)
    Button_scan.configure(image=_img2)
    Button_scan.configure(overrelief="flat")
    Button_scan.configure(pady="0")
    Button_scan.configure(relief="flat")
    Button_scan.configure(text='''Scan & Clean the USB''')

    Label_logo = tk.Label(Frame1)
    Label_logo.place(relx=0.01, rely=0.017, height=118, width=120)
    Label_logo.configure(activebackground="#f9f9f9")
    Label_logo.configure(activeforeground="black")
    Label_logo.configure(background="#103e04")
    Label_logo.configure(disabledforeground="#a3a3a3")
    Label_logo.configure(font="-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0")
    Label_logo.configure(foreground="#103e04")
    Label_logo.configure(highlightbackground="#d9d9d9")
    Label_logo.configure(highlightcolor="black")
    photo_location = os.path.join(prog_location,"usbshield0.png")

    global _img3
    _img3 = tk.PhotoImage(file=photo_location)
    Label_logo.configure(image=_img3)
    Label_logo.configure(text='''USBShield Logo''')

    Label_below = tk.Label(Frame1)
    Label_below.place(relx=0.219, rely=0.871, height=69, width=570)
    Label_below.configure(activebackground="#f9f9f9")
    Label_below.configure(activeforeground="black")
    Label_below.configure(background="#103e04")
    Label_below.configure(disabledforeground="#a3a3a3")
    Label_below.configure(font="-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    Label_below.configure(foreground="#c1edf0")
    Label_below.configure(highlightbackground="#d9d9d9")
    Label_below.configure(highlightcolor="black")
    Label_below.configure(text='''USBShield is mutually developed by Lunesys & SCO
                                    www.lunesys.com   |   info@lunesys.com   |   Islamabad, Pakistan''')

    Button_shutdown = tk.Button(Frame1)
    Button_shutdown.place(relx=0.935, rely=0.017, height=50, width=50)
    Button_shutdown.configure(activebackground="#ececec")
    Button_shutdown.configure(activeforeground="#000000")
    Button_shutdown.configure(background="#103e04")
    Button_shutdown.configure(disabledforeground="#a3a3a3")
    Button_shutdown.configure(foreground="#103e04")
    Button_shutdown.configure(highlightbackground="#d9d9d9")
    Button_shutdown.configure(highlightcolor="black")
    photo_location = os.path.join(prog_location,"shut.png")

    global _img4
    _img4 = tk.PhotoImage(file=photo_location)
    Button_shutdown.configure(image=_img4)
    Button_shutdown.configure(overrelief="flat")
    Button_shutdown.configure(pady="0")
    Button_shutdown.configure(relief="flat")
    Button_shutdown.configure(text='''Shutdown''')
    Button_shutdown.configure(command=shutDown)

    Label1_lunesys = tk.Label(Frame1)
    Label1_lunesys.place(relx=0.01, rely=0.889, height=43, width=101)
    Label1_lunesys.configure(activebackground="#f9f9f9")
    Label1_lunesys.configure(activeforeground="black")
    Label1_lunesys.configure(background="#103e04")
    Label1_lunesys.configure(disabledforeground="#a3a3a3")
    Label1_lunesys.configure(foreground="#000000")
    Label1_lunesys.configure(highlightbackground="#d9d9d9")
    Label1_lunesys.configure(highlightcolor="black")
    photo_location = os.path.join(prog_location,"lunesys.png")

    global _img5
    _img5 = tk.PhotoImage(file=photo_location)
    Label1_lunesys.configure(image=_img5)
    Label1_lunesys.configure(text='''Lunesys''')

    Label1_sco = tk.Label(Frame1)
    Label1_sco.place(relx=0.886, rely=0.889, height=43, width=101)
    Label1_sco.configure(activebackground="#f9f9f9")
    Label1_sco.configure(activeforeground="black")
    Label1_sco.configure(background="#103e04")
    Label1_sco.configure(disabledforeground="#a3a3a3")
    Label1_sco.configure(foreground="#000000")
    Label1_sco.configure(highlightbackground="#d9d9d9")
    Label1_sco.configure(highlightcolor="black")
    photo_location = os.path.join(prog_location,"sco-logo.png")

    global _img6
    _img6 = tk.PhotoImage(file=photo_location)
    Label1_sco.configure(image=_img6)
    Label1_sco.configure(text='''SCO''')

if __name__ == '__main__':
    vp_start_gui()
    root.mainloop()





