import tkinter as tk


window = tk.Tk()


#greeting = tk.Label(text="Hello, Tkinter")
# label = tk.Label(
#     text="Hello, Tkinter",
#     foreground="white",  # Set the text color to white
#     background="black"  # Set the background color to black
# )

label = tk.Label(text="Hello, Tkinter", fg="white", bg="black", width=10, height=10)
label.pack()

window.mainloop()
