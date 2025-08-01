import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Temperature convertor")
root.geometry("600x500")


def convert():
    new_temp = 0.555*(int(entry.get())-32)
    answer.config(text=f"{entry.get()}F = {new_temp}C")
    
label = tk.Label(root,text="Enter Fahrenheit:",font=10)
entry = tk.Entry(root,font=10)
button = tk.Button(root,text="Convert",font=10,command=convert)
answer = tk.Label(root,font=10)

label.place(x=50,y=50)
entry.place(x=220,y=50)
button.place(x=200,y=150)
answer.place(x=200,y=300)

root.mainloop()
