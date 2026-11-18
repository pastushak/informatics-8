# Проєкт «Розрахунок вартості розробки сайту»
# Прізвище та ім'я: ...
# Клас: 8-...

from tkinter import *
from tkinter import ttk

PRICES = {"Односторінковий (лендінг)": 4000,
          "Багатосторінковий (корпоративний)": 8000,
          "Інтернет-магазин": 26000}


def calculate(*args):
    """Перераховує вартість за всіма обраними параметрами."""
    total = PRICES[site_type.get()]
    # TODO: дизайн +50 %, адаптація +10 %
    # TODO: якщо днів менше 10 — +20 %
    # TODO: знижка з discount_box ("10%" → 10)
    result.config(text=f"Вартість: {round(total)} грн")


def hurry():
    """Кнопка «Хочу швидше»."""
    # TODO: days_scale.set(7) і перерахунок
    pass


window = Tk()
window.title("Замовлення сайту")
window.geometry("700x560")
window.resizable(False, False)
BG = "#FFE5CC"
window.configure(bg=BG)

Label(window, text="Вартість розробки сайту", font=("Arial", 20, "bold"), bg=BG).pack(pady=10)

Label(window, text="Який сайт вам потрібен?", font=("Arial", 13, "bold"), bg=BG).pack()
site_type = StringVar(value="Односторінковий (лендінг)")
for name in PRICES:
    Radiobutton(window, text=f"{name} — {PRICES[name]} грн", variable=site_type, value=name,
                bg=BG, font=("Arial", 12), command=calculate).pack(anchor="w", padx=200)

design = BooleanVar()
mobile = BooleanVar()
# TODO: два Checkbutton: «Розробити дизайн сайту (+50 %)», «Адаптація під смартфони (+10 %)»

# TODO: Scale від 7 до 14 днів (days_scale), command=calculate; days_scale.set(14)
# TODO: кнопка «Хочу швидше» (command=hurry)

# TODO: ttk.Combobox discount_box зі значеннями 0%, 10%, 20%, 30%; current(0);
#       discount_box.bind("<<ComboboxSelected>>", calculate)

result = Label(window, text="", font=("Arial", 16, "bold"), bg=BG)
result.pack(pady=10)

window.mainloop()
