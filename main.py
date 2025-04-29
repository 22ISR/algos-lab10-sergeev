import tkinter as tk


def on_button_click(value):
    if value == "Добавить":
        listbox.insert(tk.END, textbox.get("1.0", tk.END))
        textbox.delete('1.0', tk.END)
    elif value == "Удалить":
        selected = listbox.curselection()
        if selected:
            listbox.delete(selected[0])
    else:
        listbox.delete(0, tk.END)


root = tk.Tk()

root.title("Мой TODO-лист")
root.geometry("500x300")


TaskFrame = tk.Frame(root)
TaskFrame.pack()

ButtonFrame = tk.Frame(root)
ButtonFrame.pack()

ButtonFrame.columnconfigure(0, weight=1)
ButtonFrame.columnconfigure(1, weight=1)

textbox = tk.Text(TaskFrame, width=15, height=1, font=("Arial", 16))
textbox.pack(pady=10)

btn = tk.Button(TaskFrame, text="Добавить", font=("Arial", 18), command=lambda v="Добавить": on_button_click(v))
btn.pack()

listbox = tk.Listbox(TaskFrame, width=30, height=5, xscrollcommand = "_XYScrollCommand")
listbox.pack(pady=10)

delete_button = tk.Button(ButtonFrame, text="Удалить", font=("Arial", 18), command=lambda v="Удалить": on_button_click(v))
delete_button.grid(row=0, column=0, sticky="we")
btn2 = tk.Button(ButtonFrame, text="Очистить", font=("Arial", 18), command=lambda v="Очистить": on_button_click(v))
btn2.grid(row=0, column=1, sticky="we")


root.mainloop()