from tkinter import *
from tkinter import ttk
from components.file_manipulation import retrieve_file
from components.commands.clear import clear
from config.config_operations import update_value
from config.config_operations import read_data



SEARCH_KEY = "search_for"
EXCLUDE_KEY = "exclude"


def search_components(frame, key, content, text_box_list):
    """
    A function that adds a new text box and accompanying label the the given frame.

    Parmeters
              frame: The frame the components will be added to.
              key: The JSON key that the components will work with.
              content: The text that the lable will display.
              text_box_list: A list of the text boxes that have been created.
                            It is iterated over when JSON values are updated.
    Returns
              None
    """
    
    search_lable = Label(frame, text=content)
    search_lable.pack()

    # Text Box
    search_text_box = Text(frame, fg="black", height=1, width=30, relief=GROOVE, bd=2)
    search_text_box.pack()
    search_text_box.insert(INSERT, read_data(key))
    text_box_list.append((search_text_box, key))



def update_criteria(text_box_list):
    """
    Iterates over each text box in the given list and updates its accompanying JSON value.
    """
    assert text_box_list
    for i in text_box_list:
        update_value(i[1], i[0].get("1.0",'end-1c'))



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
    output = Label(second_frame, text=f"Files for the term: {read_data(SEARCH_KEY)}")
    output.pack()

    # A list that contains the text boxes that are used in the window.
    text_box_list = []

    # Components for the term that should be searched for
    search_components(second_frame, SEARCH_KEY,"File must contain: ", text_box_list)

    # Components for the term that should be excluded
    search_components(second_frame, EXCLUDE_KEY,"File must not contain: ", text_box_list)

    # This function updates the lable to the files that contain the seach term in their title.
    def clicked():
        output.configure(text=f"{retrieve_file(read_data(SEARCH_KEY), read_data(EXCLUDE_KEY))}", wraplength=300)


    ## Buttons ##
    search_button = Button(second_frame, text="Search", fg="green", command=clicked)
    search_button.pack()

    update_button = Button(second_frame, text="Update", fg="blue", 
                           command= lambda: update_criteria(text_box_list) )
    update_button.pack()

    clear_button = Button(second_frame, text="Clear", fg="red", command= lambda: clear(output))
    clear_button.pack()

    

    
    # Allow the screen to persist. Must be on the last line.
    root.mainloop()