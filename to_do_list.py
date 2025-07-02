import tkinter as tk

win=tk.Tk()
win.title("To-Do List App")
win.geometry("600x600")

tk.Label(win, text="My To-Do List", font=("Arial", 16)).pack(pady=10)

task_entry=tk.Entry(win, font=("Arial", 12))
task_entry.pack(pady=5)

task_listbox=tk.Listbox(win, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

def add_task():
    task=task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_index=task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        pass

def update_task():
    try:
        selected_index=task_listbox.curselection()[0]
        new_text=task_entry.get()
        if new_text:
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, new_text)
            task_entry.delete(0,tk.END)
    except IndexError:
        pass
        
def clear_all():
    task_listbox.delete(0, tk.END)

tk.Button(win, text="Add Task", command=add_task).pack(pady=2)
tk.Button(win, text="Delete Selected Task", command=delete_task).pack(pady=2)
tk.Button(win, text="Clear All", command=clear_all).pack(pady=2)
tk.Button(win, text="Update Task", command=update_task).pack(pady=2)

win.mainloop()
