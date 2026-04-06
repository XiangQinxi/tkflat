from tkinter import *

from tkflat import *

root = Tk()

Label(root, text="Hello, World!").pack()
Button(root, text="Click me").pack(padx=10, pady=10)
Entry(root).pack(padx=10, pady=10)
Text(root).pack(padx=10, pady=10)

root.mainloop()
