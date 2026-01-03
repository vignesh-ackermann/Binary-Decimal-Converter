import tkinter as tk
from tkinter import messagebox

# ============== Initialize main window ==================
root = tk.Tk()
root.title("Binary-Decimal Converter")
root.geometry("500x450")  # Adjusted size for table and buttons

# ============== Heading ==================
heading_label = tk.Label(
    root,
    text="Binary-Decimal Converter",
    font=('Times New Roman', 18, 'bold')
)
heading_label.pack(pady=10)

# ============== Functions ==================
history = []  # To store conversion history
saved_list = []  # To store saved values

def decimal_to_binary():
    try:
        decimal_num = int(input_field.get())
        binary_num = bin(decimal_num).replace("0b", "")
        result = f"Binary: {binary_num}"
        output_label.config(text=result)
        add_to_history(result)
    except ValueError:
        output_label.config(text="Invalid input. Please enter a decimal number.")

def binary_to_decimal():
    try:
        binary_num = input_field.get()
        if not all(bit in "01" for bit in binary_num):
            raise ValueError
        decimal_num = int(binary_num, 2)
        result = f"Decimal: {decimal_num}"
        output_label.config(text=result)
        add_to_history(result)
    except ValueError:
        output_label.config(text="Invalid input. Please enter a valid binary number.")

def clear_output():
    input_field.delete(0, tk.END)
    output_label.config(text="")

def add_to_history(value):
    if value not in history:
        history.append(value)
        update_table()

def save_value():
    val = output_label.cget("text")
    if val and val not in saved_list:
        saved_list.append(val)
        update_table()
    else:
        messagebox.showinfo("Info", "Nothing to save or value already saved.")

def remove_value():
    selected = saved_listbox.curselection()
    if selected:
        idx = selected[0]
        removed = saved_list.pop(idx)
        update_table()
        messagebox.showinfo("Removed", f"Removed: {removed}")
    else:
        messagebox.showinfo("Info", "Please select a value to remove.")

def update_table():
    # Clear history table
    for widget in history_frame.winfo_children():
        widget.destroy()
    # Display 2x2 history table
    for i, item in enumerate(history[-4:]):  # Show last 4 entries
        row = i // 2
        col = i % 2
        tk.Label(history_frame, text=item, width=25, borderwidth=1, relief="solid").grid(row=row, column=col, padx=2, pady=2)

    # Update saved listbox
    saved_listbox.delete(0, tk.END)
    for item in saved_list:
        saved_listbox.insert(tk.END, item)

# ============== Input Field ==================
input_field = tk.Entry(root, width=25, font=("Arial", 12))
input_field.pack(pady=10)

# ============== Buttons ==================
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

decimal_to_binary_button = tk.Button(
    button_frame, text="Decimal → Binary", command=decimal_to_binary, width=15
)
decimal_to_binary_button.pack(side=tk.LEFT, padx=5)

binary_to_decimal_button = tk.Button(
    button_frame, text="Binary → Decimal", command=binary_to_decimal, width=15
)
binary_to_decimal_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="Clear", command=clear_output, width=32)
clear_button.pack(pady=5)

# ============== Output Label ==================
output_label = tk.Label(root, text="", pady=10, font=("Arial", 12))
output_label.pack()

# ============== Table Frames ==================
# History Table
history_label = tk.Label(root, text="Conversion History (2x2 table):", font=("Arial", 10, "bold"))
history_label.pack(pady=5)
history_frame = tk.Frame(root)
history_frame.pack(pady=5)

# Saved List
saved_label = tk.Label(root, text="Saved Values:", font=("Arial", 10, "bold"))
saved_label.pack(pady=5)
saved_listbox = tk.Listbox(root, width=50, height=4)
saved_listbox.pack(pady=5)

# Save/Remove Buttons
save_remove_frame = tk.Frame(root)
save_remove_frame.pack(pady=5)

save_button = tk.Button(save_remove_frame, text="Save Current Value", command=save_value, width=20)
save_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(save_remove_frame, text="Remove Selected", command=remove_value, width=20)
remove_button.pack(side=tk.LEFT, padx=5)

# ============== Credit Label ==================
credit_label = tk.Label(root, text="Created by Vignesh", font=("Arial", 8))
credit_label.pack(side=tk.BOTTOM, pady=5)

# ============== Run the App ==================
root.mainloop()
