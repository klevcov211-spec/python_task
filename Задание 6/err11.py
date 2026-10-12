try:
    num1 = float(input())
    num2 = float(input())
    result = num1 / num2
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(result)
