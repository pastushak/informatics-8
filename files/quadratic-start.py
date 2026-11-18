# Проєкт «Розв'язування квадратних рівнянь» ax² + bx + c = 0
# Прізвище та ім'я: ...
# Клас: 8-...

from tkinter import *
from tkinter import messagebox
from math import sqrt


def solve():
    """Читає коефіцієнти, обчислює дискримінант і корені."""
    # TODO: зчитати a, b, c з полів (float), try / except ValueError → showerror
    # TODO: якщо a == 0 — showwarning і return
    # TODO: d = b ** 2 - 4 * a * c; три випадки: d > 0, d == 0, d < 0
    # TODO: result.config(text=...)
    pass


def clear():
    """Очищає поля і результат."""
    # TODO: entry.delete(0, END) для трьох полів, result.config(text="")
    pass


window = Tk()
window.title("Розв'язування квадратних рівнянь")
window.geometry("500x350")
window.resizable(False, False)
# TODO: колір фону

Label(window, text="ax² + bx + c = 0", font=("Arial", 20, "bold")).pack(pady=15)

frame = Frame(window)
frame.pack()
Label(frame, text="a =", font=("Arial", 14)).grid(row=0, column=0, padx=5)
entry_a = Entry(frame, width=6, font=("Arial", 14))
entry_a.grid(row=0, column=1, padx=5)
# TODO: так само b (column 2, 3) і c (column 4, 5)

# TODO: кнопки «Розрахувати» (command=solve) і «Очистити» (command=clear)

result = Label(window, text="", font=("Arial", 14))
result.pack(pady=10)

window.mainloop()
