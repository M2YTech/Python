import tkinter as tk
from tkinter import messagebox

def show_table():
    try:
        num = int(entry.get())
        output.delete('1.0', tk.END)  # Clear previous output
        for i in range(1, 11):
            output.insert(tk.END, f"{num} X {i} = {num * i}\n")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI Window
root = tk.Tk()
root.title("Multiplication Table")
root.geometry("300x350")

# Entry Label
label = tk.Label(root, text="Enter a number:")
label.pack(pady=5)

# Input Field
entry = tk.Entry(root)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Show Table", command=show_table)
button.pack(pady=5)

# Output Text Area
output = tk.Text(root, height=12, width=25)
output.pack(pady=10)

root.mainloop()
