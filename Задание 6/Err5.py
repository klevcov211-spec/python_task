s=input()
ind=int(input())
try:
    print(s[ind])
except IndexError:
    print("Индекс не в диапозоне")