import tkinter as tk
root =tk.Tk()
root.geometry("500x400")
canvas = tk.Canvas(root , width=400 , height=400)
canvas.pack()
canvas.create_line(50,50,200,50,fil="blue",width=3)
canvas.create_line(100,100,200,200,fil="red",width=5)
root.mainloop()
