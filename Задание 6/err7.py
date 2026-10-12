while True:
    try:
        n=int(input())
        print(n)
    except ValueError:
        print("Это не число попробуй еще")