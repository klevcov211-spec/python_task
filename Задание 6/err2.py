x=float(input())
y=float(input())
try:
    print(x/y)
except ZeroDivisionError:
    print("Нельзя")