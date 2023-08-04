n = int(input("Enter any integer?"))
num = 1
for i in range(0, n):
    if num < 0:
        num = 1
    for j in range(0, i + 1):
        print(num, end=" ")
        num -= 1
        if num == 1:
            num = 0
        elif num == 0:
            num == 1
        if num < 0:
            num = 1
    num = 1
    print("\r")


n = int(input("Enter any integer?"))
num = 1
for i in range(0, n):
    for j in range(0, i + 1):
        print(num, end=" ")
        num = 1 - num
    print()