import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entryInt.get()
    km_output = round(mile_input * 1.609344, 2)
    output_string.set(f"{mile_input} miles = {km_output} kilometers")

# windows
window = ttk.Window(themename="darkly")
window.title("Python GUI")
window.geometry("450x150")

# title
title_label = ttk.Label(master=window, text="Miles to kilometers", font="Calibri 24")
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entryInt)
button = ttk.Button(master = input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, 
    text="Output", 
    font="Calibri 24", 
    textvariable=output_string)
output_label.pack()

# run
window.mainloop()