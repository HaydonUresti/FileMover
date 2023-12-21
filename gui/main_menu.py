from tkinter import *


def main_menu():
    root = Tk()

    root.title("File Mover")

    # Dimensions 
    root.geometry('500x350')


    lbl = Label(root, text="A lable")
    lbl.grid()

    def clicked():
        lbl.configure(text="Click!")


    # Change the name of this button later
    button1 = Button(root, text="Click", fg="blue", command=clicked)
    
    button1.grid(column=2, row=3)


    # Allow the screen to persist. Must be on the last line.
    root.mainloop()