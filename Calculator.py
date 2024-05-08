import tkinter as codsoft
from tkinter import font

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, codsoft.END)
        entry.insert(codsoft.END, str(result))
    except Exception as e:
        entry.delete(0, codsoft.END)
        entry.insert(codsoft.END, "Error")

def clear():
    entry.delete(0, codsoft.END)

root = codsoft.Tk()
root.title("Aditya's CodSoft CalCulator")
root.geometry("300x450")
root.configure(bg="white")

label_font = font.Font(family="Segoe UI", size=16, weight="bold")
label = codsoft.Label(root, text="Aditya's CodSoft CalCulator", fg="black", font=label_font, bg="white")
label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

entry_font = font.Font(family="Segoe UI", size=20)

entry = codsoft.Entry(root, width=15, borderwidth=5, font=entry_font)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 1), (".", 5, 0), ("=", 5, 2), ("+", 5, 3)
]

button_font = font.Font(family="Segoe UI", size=12)

for (text, row, column) in buttons:
    if text.isdigit():
        button_color = "gray"
    else:
        button_color = "blue"
    button = codsoft.Button(root, text=text, padx=20, pady=20, font=button_font, bg=button_color, fg="white", bd=0, relief=codsoft.FLAT, command=lambda t=text: entry.insert(codsoft.END, t))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    button.config(highlightbackground="white")

clear_button = codsoft.Button(root, text="C", padx=20, pady=20, font=button_font, bg="red", fg="white", bd=0, relief=codsoft.FLAT, command=clear)
clear_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
clear_button.config(highlightbackground="white")

calculate_button = codsoft.Button(root, text="=", padx=20, pady=20, font=button_font, bg="green", fg="white", bd=0, relief=codsoft.FLAT, command=calculate)
calculate_button.grid(row=6, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")
calculate_button.config(highlightbackground="white")

for i in range(1, 7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
