import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Создаем вкладки
        self.tab_control = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Калькулятор")
        self.tab_control.add(self.tab2, text="Выбор")
        self.tab_control.add(self.tab3, text="Текст")

        # Создаем элементы для первой вкладки
        ttk.Label(self.tab1, text="Первое число:").grid(column=0, row=0, padx=5, pady=5)
        self.num1 = ttk.Entry(self.tab1)
        self.num1.grid(column=1, row=0, padx=5, pady=5)
        ttk.Label(self.tab1, text="Второе число:").grid(column=0, row=1, padx=5, pady=5)
        self.num2 = ttk.Entry(self.tab1)
        self.num2.grid(column=1, row=1, padx=5, pady=5)
        ttk.Label(self.tab1, text="Операция:").grid(column=0, row=2, padx=5, pady=5)
        self.operation = ttk.Combobox(self.tab1, values=["+", "-", "*", "/"])
        self.operation.current(0)
        self.operation.grid(column=1, row=2, padx=5, pady=5)
        ttk.Button(self.tab1, text="Вычислить", command=self.calculate).grid(column=0, row=3, padx=5, pady=5)
        self.result = ttk.Label(self.tab1, text="")
        self.result.grid(column=1, row=3, padx=5, pady=5)

        # Создаем элементы для второй вкладки
        self.checkbox1 = tk.BooleanVar()
        self.checkbox2 = tk.BooleanVar()
        self.checkbox3 = tk.BooleanVar()
        ttk.Checkbutton(self.tab2, text="Первый вариант", variable=self.checkbox1).grid(column=0, row=0, padx=5, pady=5)
        ttk.Checkbutton(self.tab2, text="Второй вариант", variable=self.checkbox2).grid(column=0, row=1, padx=5, pady=5)
        ttk.Checkbutton(self.tab2, text="Третий вариант", variable=self.checkbox3).grid(column=0, row=2, padx=5, pady=5)
        ttk.Button(self.tab2, text="Отправить", command=self.send_selection).grid(column=0, row=3, padx=5, pady=5)

        # Создаем элементы для третьей вкладки
        self.text = tk.Text(self.tab3)
        self.text.pack(expand=True, fill="both")
        ttk.Button(self.tab3, text="Загрузить текст", command=self.load_text).pack(padx=5, pady=5)

        # Отображаем вкладки
        self.tab_control.pack(expand=1, fill="both")

    def calculate(self):
        # Выполняем выбранную операцию и выводим результат
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())
        operation = self.operation.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        self.result.config(text=f"Результат: {result}")

    def send_selection(self):
        # Получаем выбор пользователя и выводим сообщение в зависимости от выбора
        selection = []
        if self.checkbox1.get():
            selection.append("первый")
        if self.checkbox2.get():
            selection.append("второй")
        if self.checkbox3.get():
            selection.append("третий")

        if selection:
            if len(selection) > 1:
                messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selection)} варианты")
            else:
                messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selection)} вариант")
        else:
            messagebox.showwarning("Выбор", "Вы не выбрали ни одного варианта")

    def load_text(self):
        # Открываем диалоговое окно для выбора файла
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            # Если файл выбран, загружаем его содержимое в текстовое поле
            with open(file_path, "r") as f:
                self.text.delete("1.0", "end")
                self.text.insert("1.0", f.read())

if __name__ == "__main__":
    app = Application()
    app.mainloop()