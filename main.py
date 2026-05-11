from models import Calculator

calc = Calculator("Моят калкулатор")

while True:
    a = input('Въведи първото число (или напиши "изход" за изход): ')

    if a == "изход":
        print("Довиждане!")
        break

    b = input("Въведи второто число: ")
    operation = input("Въведи действието (+ - * /): ")

    a = float(a)
    b = float(b)

    if operation == "+":
        print(f"{a} + {b} = {calc.add(a, b)}")
    elif operation == "-":
        print(f"{a} - {b} = {calc.subtract(a, b)}")
    elif operation == "*":
        print(f"{a} * {b} = {calc.multiply(a, b)}")
    elif operation == "/":
        print(f"{a} / {b} = {calc.divide(a, b)}")
    else:
        print("Невалидно действие!")
