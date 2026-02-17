import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=35, height=10)
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

root.mainloop()