a = open("C:\\Users\\LENOVO\\Downloads\\Sales.csv")
a.readline()
b = a.readlines()
add = 0
for i in b:
    c = i.split(',')
    print(c)
    add = add + int(c[3]) * int(c[4])

print("\r")
print(f"Total sum of products = {add}")
