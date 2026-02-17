##python based to do list GUI version:

# Importing tkinter library for creating GUI applications
import tkinter as tk

# Creating the main application window
root = tk.Tk()

# Setting title of the window
root.title("To-Do List")

# Setting size of the window (Width x Height)
root.geometry("300x400")

# List to store tasks (currently not used for file saving,
# but useful if we expand project later)
tasks = []

# -----------------------------
# Function to Add Task
# -----------------------------
def add_task():
    # Get text entered by user in entry box
    task = entry.get()

    # Check if input is not empty
    if task != "":
        # Insert task at the end of the listbox
        listbox.insert(tk.END, task)

        # Clear the entry box after adding task
        entry.delete(0, tk.END)


# -----------------------------
# Function to Delete Task
# -----------------------------
def delete_task():
    # Get currently selected task index
    selected = listbox.curselection()

    # If something is selected
    if selected:
        # Delete the selected task
        listbox.delete(selected)


# -----------------------------
# Entry Widget (Input Field)
# -----------------------------
# Creates text input field where user types tasks
entry = tk.Entry(root, width=25)
entry.pack(pady=10)  # Adds vertical spacing


# -----------------------------
# Add Button
# -----------------------------
# When clicked, it calls add_task function
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()


# -----------------------------
# Listbox Widget
# -----------------------------
# Displays the list of tasks
listbox = tk.Listbox(root, width=35, height=10)
listbox.pack(pady=10)


# -----------------------------
# Delete Button
# -----------------------------
# When clicked, it calls delete_task function
delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()


# Running the application (keeps window open)
root.mainloop()

