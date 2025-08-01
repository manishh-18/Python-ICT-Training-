import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")
    
root = tk.Tk()
root.title("Simple GUI")
root.geometry("600x500")

label = tk.Label(root,text="Hello, Manish!",font=10)
label.pack(pady=20)

button = tk.Button(root,text="Click me",command=on_button_click,font=10)
button.pack(pady=20)

root.mainloop()
