import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Hello! This is a minimal GUI", font=("Arial", 12))
label.pack(pady=20)

# Add a button that closes the window
button = tk.Button(root, text="Click Me to Exit", command=root.destroy)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
