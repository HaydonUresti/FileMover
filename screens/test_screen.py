import tkinter as tk
from tkinter import ttk

def test_screen():
    def on_configure(event):
        # Update the scroll region to encompass the inner frame
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Create the main window
    root = tk.Tk()
    root.title("Scrollable Window Example")

    # Create a Canvas widget for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Scrollbar widget and associate it with the Canvas
    scrollbar = ttk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)