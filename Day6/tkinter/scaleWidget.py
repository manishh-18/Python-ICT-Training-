import tkinter as tk
from tkinter import PhotoImage

def on_scale_change(value):
    label_value.config(text=f"Value : {value}")
    
root = tk.Tk()
root.title("Temperature convertor")
root.geometry("600x500")

frame = tk.Frame(root)
scale = tk.Scale(frame,from_=0,to=100,orient=tk.HORIZONTAL,command=on_scale_change,bg="black",font=10)
scale.pack()

label_value = tk.Label(root,text="Value: 0")
label_value.pack(pady=10)

frame.pack(padx=20,pady=20)

root.mainloop()
