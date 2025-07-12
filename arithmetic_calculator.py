import tkinter as tk

win=tk.Tk()
win.title("Arithmetic Calculator")
win.geometry("1000x1000")

tk.Label(win, text="Arithmetic Calculator", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10) 

tk.Label(win, text="Number 1:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_num1=tk.Entry(win)
entry_num1.grid(row=1, column=1, padx=10)

tk.Label(win, text="Number 2:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_num2=tk.Entry(win)
entry_num2.grid(row=2, column=1, padx=10)

tk.Label(win, text="Operation:").grid(row=3, column=0, sticky="e", padx=10, pady=5)

operation=tk.StringVar(value="None")

operation_frame=tk.Frame(win)
operation_frame.grid(row=3, column=1, columnspan=4, pady=5)

tk.Radiobutton(operation_frame, text="+", variable=operation, value="+").pack(side="left", padx=5)
tk.Radiobutton(operation_frame, text="-", variable=operation, value="-").pack(side="left", padx=5)
tk.Radiobutton(operation_frame, text="*", variable=operation, value="*").pack(side="left", padx=5)
tk.Radiobutton(operation_frame, text="/", variable=operation, value="/").pack(side="left", padx=5)


def show_result():
    if operation.get()=="+":
        label.config(text=f"Sum: {float(entry_num1.get())+float(entry_num2.get())}")
    elif operation.get()=="-":
        label.config(text=f"Subtraction: {float(entry_num1.get())-float(entry_num2.get())}")
    elif operation.get()=="*":
        label.config(text=f"Product: {float(entry_num1.get())*float(entry_num2.get())}")
    elif operation.get()=="/":
        label.config(text=f"Divide: {float(entry_num1.get())/float(entry_num2.get())}")
    else:
        label.config(text="Operation not found")

tk.Button(win, text="Calculate", command=show_result).grid(row=4, column=1, columnspan=2, pady=5)
label=tk.Label(win, text="")
label.grid(row=5, column=1, columnspan=2, pady=5)

win.mainloop()



          



