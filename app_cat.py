from tkinter import *
from tkinter.ttk import *


def set_first():
    number_1 = num21.get().replace(" ", "")
    number_one = number_1.isdigit()
    number_2 = num31.get().replace(",", ".").replace(" ", "")
    number_2_int_positive = number_2.isdigit()
    number_2_float_positive = number_2.find(".") != -1 and number_2.replace(".", "", 1).isdigit()
    number_two = number_2_int_positive or number_2_float_positive
    number_3 = num41.get().replace(" ", "")
    number_3_int_positive = number_3.isdigit()
    number_3_not_zero = number_3.replace("0", "").isdigit()
    number_three = number_3_int_positive and number_3_not_zero
    if num11.get().strip() and number_one and number_two and number_three:
        total_first.set(int(number_1)*float(number_2)/int(number_3))
    elif num11.get().strip() and num21.get().strip() and num31.get().strip() and num41.get().strip():
        total_first.set("Error")
    elif not(num11.get().strip() or num21.get().strip() or num31.get().strip() or num41.get().strip()):
        total_first.set("")
    else:
        total_first.set("Fill all the fills of line")


def set_second():
    number_1 = num22.get().replace(" ", "")
    number_one = number_1.isdigit()
    number_2 = num32.get().replace(",", ".").replace(" ", "")
    number_2_int_positive = number_2.isdigit()
    number_2_float_positive = number_2.find(".") != -1 and number_2.replace(".", "", 1).isdigit()
    number_two = number_2_int_positive or number_2_float_positive
    number_3 = num42.get().replace(" ", "")
    number_3_int_positive = number_3.isdigit()
    number_3_not_zero = number_3.replace("0", "").isdigit()
    number_three = number_3_int_positive and number_3_not_zero
    if num12.get().strip() and number_one and number_two and number_three:
        total_second.set(int(number_1) * float(number_2) / int(number_3))
    elif num12.get().strip() and num22.get().strip() and num32.get().strip() and num42.get().strip():
        total_second.set("Error")
    elif not(num12.get().strip() or num22.get().strip() or num32.get().strip() or num42.get().strip()):
        total_second.set("")
    else:
        total_second.set("Fill all the fills of line")


def set_third():
    number_1 = num23.get().replace(" ", "")
    number_one = number_1.isdigit()
    number_2 = num33.get().replace(",", ".").replace(" ", "")
    number_2_int_positive = number_2.isdigit()
    number_2_float_positive = number_2.find(".") != -1 and number_2.replace(".", "", 1).isdigit()
    number_two = number_2_int_positive or number_2_float_positive
    number_3 = num43.get().replace(" ", "")
    number_3_int_positive = number_3.isdigit()
    number_3_not_zero = number_3.replace("0", "").isdigit()
    number_three = number_3_int_positive and number_3_not_zero
    if num13.get().strip() and number_one and number_two and number_three:
        total_third.set(int(number_1) * float(number_2) / int(number_3))
    elif num13.get().strip() and num23.get().strip() and num33.get().strip() and num43.get().strip():
        total_third.set("Error")
    elif not(num13.get().strip() or num23.get().strip() or num33.get().strip() or num43.get().strip()):
        total_third.set("")
    else:
        total_third.set("Fill all the fills of line")


def count_fourth():
    set_first()
    set_second()
    set_third()
    number_one = total_first.get().find(".") != -1 and total_first.get().replace(".", "", 1).isdigit() or \
                 not total_first.get().strip()
    number_two = total_second.get().find(".") != -1 and total_second.get().replace(".", "", 1).isdigit() or \
                 not total_second.get().strip()
    number_three = total_third.get().find(".") != -1 and total_third.get().replace(".", "", 1).isdigit() or \
                   not total_third.get().strip()
    if number_one and number_two and number_three:
        total_fourth.set((float(total_first.get().replace("", "0")) + float(total_second.get().replace("", "0"))
                          + float(total_third.get().replace("", "0"))) * 365)
    elif num13.get().strip() and num23.get().strip() and num33.get().strip() and num43.get().strip():
        total_fourth.set("Error")
    elif not(total_first.get() or total_second.get() or total_third.get()):
        total_fourth.set(0)


def count_fifth():
    total_fifth.set(0)
    count_fourth()
    number = number_of_years.get().replace(" ", "").replace(",", ".")
    number_int_positive = number.isdigit()
    number_float_positive = number.find(".") != -1 and number.replace(".", "", 1).isdigit()
    if not number_of_years.get().strip():
        number_of_years.set("Enter the years")
    elif number_int_positive or number_float_positive:
        total_fifth.set(float(number) * float(total_fourth.get()))


root = Tk()
root.title("Calculator for cat")
Label(text="Товар").grid(column=1, row=0)
label_quantity = Label(text="Кол-во ед.").grid(column=2, row=0)
label_price_one = Label(text="Цена за ед.").grid(column=3, row=0)
label_days = Label(text="Кол-во дней.").grid(column=4, row=0)
label_price = Label(text="Общая цена").grid(column=6, row=0)
num11 = StringVar()
entry_11 = Entry(textvariable=num11)
entry_11.grid(column=1, row=1)
num21 = StringVar()
num21.set(0)
entry_21 = Entry(textvariable=num21)
entry_21.grid(column=2, row=1)
num31 = StringVar()
num31.set(3)
entry_31 = Entry(textvariable=num31)
entry_31.grid(column=3, row=1)
num41 = StringVar()
num41.set(4)
entry_41 = Entry(textvariable=num41)
entry_41.grid(column=4, row=1)
total_first = StringVar()
total_first.set(0)
entry_61 = Entry(textvariable=total_first)
entry_61.grid(column=6, row=1)
button_1 = Button(text="=", command=set_first)
button_1.grid(column=5, row=1)

num12 = StringVar()
entry_12 = Entry(textvariable=num12)
entry_12.grid(column=1, row=2)
num22 = StringVar()
num22.set(6)
entry_22 = Entry(textvariable=num22)
entry_22.grid(column=2, row=2)
num32 = StringVar()
num32.set(3)
entry_32 = Entry(textvariable=num32)
entry_32.grid(column=3, row=2)
num42 = StringVar()
num42.set(9)
entry_42 = Entry(textvariable=num42)
entry_42.grid(column=4, row=2)
total_second = StringVar()
total_second.set(0)
entry_62 = Entry(textvariable=total_second)
entry_62.grid(column=6, row=2)
button_2 = Button(text="=", command=set_second)
button_2.grid(column=5, row=2)

num13 = StringVar()
entry_13 = Entry(textvariable=num13)
entry_13.grid(column=1, row=3)
num23 = StringVar()
num23.set(1)
entry_23 = Entry(textvariable=num23)
entry_23.grid(column=2, row=3)
num33 = StringVar()
num33.set(4)
entry_33 = Entry(textvariable=num33)
entry_33.grid(column=3, row=3)
num43 = StringVar()
num43.set(8)
entry_43 = Entry(textvariable=num43)
entry_43.grid(column=4, row=3)
total_third = StringVar()
total_third.set(0)
entry_63 = Entry(textvariable=total_third)
entry_63.grid(column=6, row=3)
button_3 = Button(text="=", command=set_third)
button_3.grid(column=5, row=3)

Label(text="Всего затраты за год", justify=LEFT).grid(column=0, row=4, columnspan=4)
button_6 = Button(text="=", command=count_fourth)
button_6.grid(column=5, row=4)
total_fourth = StringVar()
total_fourth.set(0)
entry_for_year = Entry(textvariable=total_fourth)
entry_for_year.grid(column=6, row=4)

Label(text="Количество лет", justify=LEFT).grid(column=0, row=5, columnspan=4)
number_of_years = StringVar()
number_of_years.set("")
entry_number_of_years = Entry(textvariable=number_of_years)
entry_number_of_years.grid(column=6, row=5)

Label(text="Общее содержание за все годы", justify=LEFT).grid(column=0, row=6, columnspan=4)
button_6 = Button(text="Итого", command=count_fifth)
button_6.grid(column=5, row=6)
total_fifth = StringVar()
total_fifth.set(0)
entry_total = Entry(textvariable=total_fifth)
entry_total.grid(column=6, row=6)
root.mainloop()
