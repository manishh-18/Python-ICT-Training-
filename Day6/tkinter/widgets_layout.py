import tkinter as tk

root = tk.Tk()
root.title("Grid Layout with Different Widgets")
root.geometry("500x700")

# Create widgets with correct 'text' keyword
label = tk.Label(root, text="This is a Label", bg="lightblue")
button = tk.Button(root, text="Click Me")
entry = tk.Entry(root)
text = tk.Text(root, height=5, width=60)
checkbutton = tk.Checkbutton(root, text="Check Me")
radiobutton1 = tk.Radiobutton(root, text="Option 1", value=1)
radiobutton2 = tk.Radiobutton(root, text="Option 2", value=2)

# Place widgets using grid
label.grid(row=0, column=0, padx=10, pady=10, sticky="s")
button.grid(row=0, column=1, padx=10, pady=10, sticky="e")
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="es")
checkbutton.grid(row=3, column=0, padx=10, pady=10, sticky="w")
radiobutton1.grid(row=3, column=1, padx=10, pady=10, sticky="e")
radiobutton2.grid(row=4, column=1, padx=10, pady=10, sticky="e")

# Configure grid columns to expand
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)

# Run the main loop
root.mainloop()
