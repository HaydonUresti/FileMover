from tkinter import *
from components.retrieve_file import retrieve_file


def main_menu():
    root = Tk()

    root.title("File Mover")

    # Dimensions 
    root.geometry('500x350')


    lbl = Label(root, text="A lable")
    lbl.grid()

    def on_configure(event):
    # Update the scroll region to encompass the inner frame
        canvas.configure(scrollregion=canvas.bbox("all"))

    def clicked():
        lbl.configure(text=f"{retrieve_file()}", wraplength=300)


    
    # Change the name of this button later
    button1 = Button(root, text="Click", fg="blue", command=clicked)
    
    button1.grid(column=2, row=3)


    # Allow the screen to persist. Must be on the last line.
    root.mainloop()