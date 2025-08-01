import tkinter as tk

root = tk.Tk()
root.title("Hello, this is my page using tkinter")
root.geometry("600x500")

label1 = tk.Label(root,text="Label 1",bg='red',height=10,width=10)
label1.place(x=50,y=50)

label2 = tk.Label(root,text="Label 2",bg='green',height=10,width=10)
label2.place(x=150,y=100)

root.mainloop()