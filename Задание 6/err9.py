try:
    age = int(input())
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
    print("Принято",age)
except ValueError as e:
    if str(e) == "Возраст вне допустимого диапазона":
        print(e)
    else:
        print("Отклонено: Введено не целое число")
