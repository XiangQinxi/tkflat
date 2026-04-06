from tkinter import *  # NOQA

from tkflat import *

Theme.using_theme = "dark"

root = Tk()

frame = Frame(root)

Label(frame, text="tkflat.Label").pack()
Button(frame, text="tkflat.Button", command=lambda: print("Button is clicked")).pack(
    padx=10, pady=10
)
Entry(frame).pack(padx=10, pady=10)
Text(frame).pack(padx=10, pady=10)

frame.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
