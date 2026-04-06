from tkinter import *  # NOQA

from tkflat import *

Theme.using_theme = "dark"

root = Tk()

Label(root, text="tkflat.Label").pack()
Button(root, text="tkflat.Button", command=lambda: print("Button is clicked")).pack(
    padx=10, pady=10
)
Entry(root).pack(padx=10, pady=10)
Text(root).pack(padx=10, pady=10)

root.mainloop()
