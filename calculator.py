import tkinter as tk
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry.get() + text)
root = tk.Tk()
root.title("Calculator")
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=8, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
row_val = 1
col_val = 0
for text in button_texts:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18))
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3: