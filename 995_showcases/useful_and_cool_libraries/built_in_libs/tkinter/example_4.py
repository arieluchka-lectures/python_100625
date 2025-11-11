import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_all():
    listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")

# Title label
title = tk.Label(root, text="My To-Do List", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Frame for entry and add button
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Entry field
entry = tk.Entry(input_frame, font=("Arial", 12), width=25)
entry.pack(side=tk.LEFT, padx=5)

# Add button
add_btn = tk.Button(input_frame, text="Add Task", font=("Arial", 10), command=add_task)
add_btn.pack(side=tk.LEFT)

# Listbox to display tasks
listbox = tk.Listbox(root, font=("Arial", 11), height=15, selectmode=tk.SINGLE)
listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Frame for action buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Delete and clear buttons
delete_btn = tk.Button(button_frame, text="Delete Task", font=("Arial", 10), command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(button_frame, text="Clear All", font=("Arial", 10), command=clear_all)
clear_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()