import tkinter as tk

root = tk.Tk()
root.title("Hello, this is my page using tkinter")
root.geometry("600x500")

label1 = tk.Label(root,text="Label 1",bg='cyan')
label1.pack(fill=tk.BOTH, expand=True)

label2 = tk.Label(root,text="Label 2",bg='green')
label2.pack(fill=tk.BOTH, expand=True)

root.mainloop()