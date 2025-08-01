import tkinter as tk
root = tk.Tk()
root.title("Welcome to Python GUI")
root.geometry("500x500")

frame_top = tk.Frame(root)
frame_bottom = tk.Frame(root)

frame_top.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
frame_bottom.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

label1=tk.Label(frame_top,text="label1")
label2=tk.Label(frame_top,text= "label2")
label3=tk.Label(frame_bottom,text="label3")
label4=tk.Label(frame_bottom,text="label4")

label1.pack(side=tk.LEFT)
label2.pack(side=tk.RIGHT)
label3.grid(row=0,column=0)
label4.grid(row=2,column=2)

root.mainloop()