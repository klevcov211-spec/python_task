
try:
    s = input()
    ind = int(input())
    print(s[ind])
except ValueError:
    print("Число введи")
except IndexError:
    print("Индекс не в диапозоне")