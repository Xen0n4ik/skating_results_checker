from tkinter import *
from tkinter.messagebox import *


class FigureSkatingApp:
    def __init__(self):
        self.win = Tk()
        self.win.title('Фигуристы')
        self.surname = []
        self.ball = []
        self.setup_ui()

    def setup_ui(self):
        Label(self.win, text='Введите кортеж из 10 фигуристов и их баллов').grid(row=0, column=0)

        Button(self.win, text='Задать кортеж', command=self.zadan).grid(row=1, column=0)
        Button(self.win, text='Проверить результаты', command=self.rez).grid(row=1, column=1)

        Label(self.win, text='Фамилии и баллы').grid(row=3, column=0)
        Label(self.win, text='Прошли', width=30).grid(row=3, column=1)

        self.txt1 = Text(self.win, width=20, height=5, wrap=WORD)
        self.txt1.grid(row=4, column=0)
        self.txt2 = Text(self.win, width=20, height=5, wrap=WORD)
        self.txt2.grid(row=4, column=1)

        Button(self.win, text='Очистить', width=20, command=self.clear).grid(row=5, columnspan=2)

    def rez(self):
        default_data = ('Безматерных', 5.7, 'Волчкова', 2.4, 'Госвияни', 3.1,
                        'Злобина', 4.5, 'Квителашвили', 5.2, 'Кондратюк', 1.3,
                        'Лутай', 5.9, 'Маисурадзе', 2.7, 'Мишкутёнок', 3.2, 'Обсертас', 1.1)

        input_text = self.txt1.get(0.0, END).strip()
        data = input_text.split() if input_text else default_data

        passed = [data[i] for i in range(0, len(data), 2) if float(data[i + 1]) > 3.9]

        self.txt2.delete(0.0, 'end')
        self.txt2.insert(END, '\n'.join(passed))

    def clear(self):
        self.txt1.delete(0.0, 'end')
        self.txt2.delete(0.0, 'end')

    def sled(self):
        f = self.fam.get().strip()
        b = self.bal.get().strip()

        if not f or not b:
            showerror('Ошибка', 'Все поля должны быть заполнены')
            return

        if not b.replace('.', '').isdigit():
            showerror('Ошибка', 'Неправильный ввод данных')
            return

        self.ball.append(float(b))
        self.surname.append(f)
        self.fam.delete(0, 'end')
        self.bal.delete(0, 'end')
        self.txt1.insert(END, f'{f} {b}\n')

    def konec(self):
        self.top.destroy()

    def zadan(self):
        self.top = Toplevel(self.win)
        self.top.geometry('220x70+300+300')

        Label(self.top, text='Введите фамилию', width=15).grid(row=0, column=0)
        self.fam = Entry(self.top, width=15)
        self.fam.grid(row=0, column=1)

        Label(self.top, text='Введите балл').grid(row=1, column=0)
        self.bal = Entry(self.top, width=15)
        self.bal.grid(row=1, column=1)

        Button(self.top, text='Следующий', command=self.sled).grid(row=2, column=0)
        Button(self.top, text='Завершить ввод', command=self.konec).grid(row=2, column=1)

    def run(self):
        self.win.mainloop()


if __name__ == "__main__":
    app = FigureSkatingApp()
    app.run()