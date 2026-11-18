# Проєкт «PyPizza» — замовлення піци у трьох вікнах
# Прізвище та ім'я: ...
# Клас: 8-...

from tkinter import *
from tkinter import messagebox

BG = "#FFF3E0"
BASES = {"Тонка основа": 100, "Класична основа": 120, "Сирна основа": 150}
TOPPINGS = {"Сир": 20, "М'ясо": 30, "Овочі": 15}
DRINKS = {"Без напою": 0, "Кока-кола": 15, "Сік": 25, "Мінеральна вода": 20}


def open_pizza():
    """Вікно 2: конструктор піци."""
    pizza = Toplevel(start)
    pizza.title("Створи свою піцу")
    pizza.geometry("420x520")
    pizza.configure(bg=BG)

    base = StringVar(value="Класична основа")
    toppings = {name: BooleanVar() for name in TOPPINGS}
    drink = StringVar(value="Без напою")

    def price():
        total = BASES[base.get()]
        # TODO: додати вартість обраних начинок і напою
        return total

    def update():
        price_label.config(text=f"Вартість: {price()} грн")

    Label(pizza, text="Основа:", font=("Calibri", 14, "bold"), bg=BG).pack(anchor="w", padx=20)
    for name, cost in BASES.items():
        Radiobutton(pizza, text=f"{name} ({cost} грн)", variable=base, value=name, bg=BG,
                    command=update).pack(anchor="w", padx=40)
    # TODO: «Начинка:» — Checkbutton для кожного з TOPPINGS
    # TODO: «Напій:» — Radiobutton для кожного з DRINKS

    price_label = Label(pizza, text="", font=("Calibri", 16, "bold"), bg=BG)
    price_label.pack(pady=10)
    Button(pizza, text="Оформити замовлення", command=lambda: open_order(price())).pack()
    update()


def open_order(total):
    """Вікно 3: контактні дані."""
    # TODO: Toplevel «Оформлення замовлення», сума до сплати,
    #       поля Ім'я, Телефон, Адреса, кнопка «Підтвердити»
    # TODO: порожні поля → showwarning; інакше showinfo «..., замовлення прийнято!» і destroy()
    pass


start = Tk()
start.title("PyPizza")
start.geometry("400x260")
start.configure(bg=BG)
Label(start, text="PyPizza", font=("Calibri", 28, "bold"), bg=BG, fg="#C0392B").pack(pady=20)
# TODO: підзаголовок і кнопки «Піца» (open_pizza) та «Суші»
start.mainloop()
