from Tkinter import *

root = Tk()

labelframe = LabelFrame(root, text="Zero to Hero")
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text="You Can be the Hero of Your Own World!")
left.pack()

root.mainloop()
