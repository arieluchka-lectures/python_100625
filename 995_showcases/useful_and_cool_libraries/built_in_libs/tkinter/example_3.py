import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Text Editor - New File")

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(1.0, file.read())
            root.title(f"Text Editor - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"Text Editor - {file_path}")
            messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

# Create main window
root = tk.Tk()
root.title("Text Editor")
root.geometry("600x500")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create scrolled text area
text_area = scrolledtext.ScrolledText(root, font=("Arial", 11), wrap=tk.WORD, undo=True)
text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()