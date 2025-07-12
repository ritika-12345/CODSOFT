import tkinter as tk
win = tk.Tk()
win.title("Contact Book")
win.geometry("800x700")

tk.Label(win, text="Contact book", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(win, text="Name:").grid(row=1, column=0, pady=5, padx=10)
name=tk.Entry(win)
name.grid(row=1, column=1, pady=5, padx=10)

tk.Label(win, text="Phone No.:").grid(row=2, column=0, pady=5, padx=10)
phone_no=tk.Entry(win)
phone_no.grid(row=2, column=1, pady=5, padx=10)

tk.Label(win, text="Email:").grid(row=3, column=0, padx=10, pady=5)
email=tk.Entry(win)
email.grid(row=3, column=1, padx=10, pady=5)

tk.Label(win, text="Address:").grid(row=4, column=0, padx=10, pady=5)
address=tk.Entry(win)
address.grid(row=4, column=1, padx=10, pady=5)

contact_list=tk.Listbox(win, width=50, height=20, font=("Arial", 12))
contact_list.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

def add_contact():
    names=name.get()
    phone=phone_no.get()
    emai=email.get()
    addr=address.get()
    if names and phone and emai and addr:
        contact_list.insert(tk.END,f"{names} | {phone} | {emai} | {addr}")
        name.delete(0, tk.END)
        phone_no.delete(0, tk.END)
        email.delete(0, tk.END)
        address.delete(0, tk.END)
tk.Button(win, text="Add",  command=add_contact).grid(row=6, column=0, pady=5, padx=10)

def delete_contact():
    try:
        selected_contact=contact_list.curselection()[0]
        contact_list.delete(selected_contact)
    except IndexError:
        pass
tk.Button(win, text="Delete", command=delete_contact).grid(row=6, column=1, pady=5, padx=10)

search_entry=tk.Entry(win, width=30)
search_entry.grid(row=7, column=0, padx=10, pady=5)

def search_contact():
    query = search_entry.get().lower()
    results=[]
    for i in range(contact_list.size()):
        if query in contact_list.get(i).lower():
            results.append(contact_list.get(i))
    if results:
        contact_list.delete(0, tk.END)
        for res in results:
            contact_list.insert(tk.END, res)
    else:
        contact_list.delete(0, tk.END)
        contact_list.insert(tk.END, "No match found.")
tk.Button(win, text="Search", command=search_contact).grid(row=7, column=1)

def update_contact():
    try:
        selected_contact=contact_list.curselection()[0]
        contact_text=contact_list.get(selected_contact)
        contact_parts=contact_text.split(" | ")
        names=contact_parts[0]
        phone=contact_parts[1]
        emai=contact_parts[2]
        addr=" ".join(contact_parts[3:])
        name.delete(0, tk.END)
        name.insert(0,names)
        phone_no.delete(0, tk.END)
        phone_no.insert(0,phone)
        email.delete(0, tk.END)
        email.insert(0,emai)
        address.delete(0, tk.END)
        address.insert(0,addr)
        contact_list.delete(selected_contact)
    except IndexError:
        pass
tk.Button(win, text="Update", command=update_contact).grid(row=6, column=2, pady=5, padx=10)

win.mainloop()
