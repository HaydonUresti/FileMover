from tkinter import *
from tkinter import ttk
from components.retrieve_file import retrieve_file
from components.Buttons.clear import clear
from config.config_operations import update_value
from config.config_operations import read_data


SEARCH_KEY = "search_for"


def main_menu():
    root = Tk()
    root.title("File Mover")

    # Dimensions 
    root.geometry('800x650')

    # Frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH,expand=1)

    # Scroll Bar Frame
    scroll_frame = Frame(main_frame)
    scroll_frame.pack(fill=X,side=BOTTOM)

    # Canvas
    main_canvas = Canvas(main_frame)
    main_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    x_scrollbar = ttk.Scrollbar(scroll_frame,orient=HORIZONTAL,command=main_canvas.xview)

    x_scrollbar.pack(side=BOTTOM,fill=X)

    y_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=main_canvas.yview)
    y_scrollbar.pack(side=RIGHT,fill=Y)

    # Configure the canvas
    main_canvas.configure(xscrollcommand=x_scrollbar.set)
    main_canvas.configure(yscrollcommand=y_scrollbar.set)
    main_canvas.bind("<Configure>",lambda e: main_canvas.config(scrollregion= main_canvas.bbox(ALL))) 


    # Create Another Frame INSIDE the Canvas
    second_frame = Frame(main_canvas)

    # Add that New Frame a Window In The Canvas
    main_canvas.create_window((0,0),window= second_frame, anchor="nw")

    # Labels
    lbl = Label(second_frame, text="A lable")
    lbl.pack()

    # This function updates the lable to the files that contain the seach term in their title.
    def clicked():
        lbl.configure(text=f"{retrieve_file(read_data(SEARCH_KEY))}", wraplength=300)

    # Text Box
    search_term = read_data(SEARCH_KEY)
    folder_text_box = Text(second_frame, fg="grey", height=5, width=30, relief=GROOVE, bd=2)
    folder_text_box.pack()
    folder_text_box.insert(INSERT, search_term)

    ## Buttons ##
    activate_button = Button(second_frame, text="Click", fg="blue", command=clicked)
    activate_button.pack()

    clear_button = Button(second_frame, text="Clear", fg="red", command= lambda: clear(lbl))
    clear_button.pack()

    update_button = Button(second_frame, text="Update", fg="green", 
                           command= lambda: update_value(SEARCH_KEY, folder_text_box.get("1.0",'end-1c')))
    update_button.pack()

    
    # Allow the screen to persist. Must be on the last line.
    root.mainloop()