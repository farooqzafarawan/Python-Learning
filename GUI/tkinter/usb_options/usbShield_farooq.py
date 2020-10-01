#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk

py3 = True

#import usbshield2_support

root = tk.Tk()


def vp_start_gui():
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'

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
    Frame1.place(relx=0.01, rely=0.017, relheight=0.975, relwidth=0.981)

    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#103e04")
    Frame1.configure(highlightbackground="#d9d9d9")
    Frame1.configure(highlightcolor="black")

    Button_shutdown = tk.Button(Frame1)
    Button_shutdown.place(relx=0.925, rely=0.017, height=64, width=64)
    Button_shutdown.configure(activebackground="#ececec")
    Button_shutdown.configure(activeforeground="#000000")
    Button_shutdown.configure(background="#c1edf0")
    Button_shutdown.configure(disabledforeground="#a3a3a3")
    Button_shutdown.configure(foreground="#103e04")
    Button_shutdown.configure(highlightbackground="#d9d9d9")
    Button_shutdown.configure(highlightcolor="black")
    Button_shutdown.configure(overrelief="flat")
    Button_shutdown.configure(pady="0")
    Button_shutdown.configure(relief="flat")
    Button_shutdown.configure(text='''Shutdown''')

    Button_info = tk.Button(Frame1)
    Button_info.place(relx=0.846, rely=0.017, height=64, width=64)
    Button_info.configure(activebackground="#ececec")
    Button_info.configure(activeforeground="#000000")
    Button_info.configure(background="#c1edf0")
    Button_info.configure(disabledforeground="#a3a3a3")
    Button_info.configure(foreground="#103e04")
    Button_info.configure(highlightbackground="#d9d9d9")
    Button_info.configure(highlightcolor="black")
    Button_info.configure(overrelief="flat")
    Button_info.configure(pady="0")
    Button_info.configure(relief="flat")
    Button_info.configure(text='''Info''')

    Button_erase = tk.Button(Frame1)
    Button_erase.place(relx=0.1, rely=0.274, height=180, width=346)
    Button_erase.configure(activebackground="#ececec")
    Button_erase.configure(activeforeground="#000000")
    Button_erase.configure(background="#c1edf0")
    Button_erase.configure(disabledforeground="#a3a3a3")
    Button_erase.configure(font="-family {Segoe UI} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Button_erase.configure(foreground="#103e04")
    Button_erase.configure(highlightbackground="#d9d9d9")
    Button_erase.configure(highlightcolor="#000000")
    Button_erase.configure(overrelief="flat")
    Button_erase.configure(pady="0")
    Button_erase.configure(relief="flat")
    Button_erase.configure(text='''Secure Erase / Wipe the USB''')

    Button_scan = tk.Button(Frame1)
    Button_scan.place(relx=0.557, rely=0.274, height=180, width=347)
    Button_scan.configure(activebackground="#ececec")
    Button_scan.configure(activeforeground="#000000")
    Button_scan.configure(background="#c1edf0")
    Button_scan.configure(disabledforeground="#a3a3a3")
    Button_scan.configure(font="-family {Segoe UI} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Button_scan.configure(foreground="#103e04")
    Button_scan.configure(highlightbackground="#d9d9d9")
    Button_scan.configure(highlightcolor="#000000")
    Button_scan.configure(overrelief="flat")
    Button_scan.configure(pady="0")
    Button_scan.configure(relief="flat")
    Button_scan.configure(text='''Scan & Clean the USB''')

    Label_logo = tk.Label(Frame1)
    Label_logo.place(relx=0.01, rely=0.017, height=120, width=120)
    Label_logo.configure(activebackground="#f9f9f9")
    Label_logo.configure(activeforeground="black")
    Label_logo.configure(background="#c1edf0")
    Label_logo.configure(disabledforeground="#a3a3a3")
    Label_logo.configure(font="-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0")
    Label_logo.configure(foreground="#103e04")
    Label_logo.configure(highlightbackground="#d9d9d9")
    Label_logo.configure(highlightcolor="black")
    Label_logo.configure(text='''USBShield Logo''')

    Label_below = tk.Label(Frame1)
    Label_below.place(relx=0.02, rely=0.872, height=70, width=970)
    Label_below.configure(activebackground="#f9f9f9")
    Label_below.configure(activeforeground="black")
    Label_below.configure(background="#103e04")
    Label_below.configure(disabledforeground="#a3a3a3")
    Label_below.configure(font="-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    Label_below.configure(foreground="#c1edf0")
    Label_below.configure(highlightbackground="#d9d9d9")
    Label_below.configure(highlightcolor="black")
    Label_below.configure(text='''The USBSHield is a dedicated system for secure erasing / wiping or scanning and cleaning the USB's against viruses
                                USBShield is mutually designed by Lunesys & SCO 
                                www.lunesys.com   |   info@lunesys.com   |   Islamabad, Pakistan''')

if __name__ == '__main__':
    vp_start_gui()
    root.mainloop()





