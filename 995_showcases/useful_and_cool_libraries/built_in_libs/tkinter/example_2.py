import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Create entry field
entry = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons
row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, font=("Arial", 14), command=calculate)
    elif button == 'C':
        btn = tk.Button(root, text=button, font=("Arial", 14), command=clear)
    else:
        btn = tk.Button(root, text=button, font=("Arial", 14),
                       command=lambda b=button: button_click(b))

    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()