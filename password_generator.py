import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())

root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x250")
root.configure(bg="#1e1e2f")

title = tk.Label(root,text="Password Generator",font=("Arial",18,"bold"),bg="#1e1e2f",fg="white")
title.pack(pady=10)

tk.Label(root,text="Password Length",bg="#1e1e2f",fg="white").pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Button(root,text="Generate Password",bg="#4CAF50",fg="white",command=generate_password).pack(pady=10)

result_entry = tk.Entry(root,width=30,font=("Arial",12))
result_entry.pack(pady=10)

tk.Button(root,text="Copy Password",bg="#2196F3",fg="white",command=copy_password).pack()

root.mainloop()