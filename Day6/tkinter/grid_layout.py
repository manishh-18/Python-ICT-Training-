import tkinter as tk

root = tk.Tk()
root.title("Hello, this is my page using tkinter")
root.geometry("600x500")

label1 = tk.Label(root,text="Label 1",bg='cyan',height=10,width=10)
label1.grid(row=0,column=0)

label2 = tk.Label(root,text="Label 2",bg='green',height=10,width=10)
label2.grid(row=1,column=1)

root.mainloop()