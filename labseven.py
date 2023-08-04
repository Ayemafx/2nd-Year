# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# n = int(input("Enter a number to calculate its factorial"))
# result = factorial(n)
# print(f"The factorial of {n} is {result}")
#
# def fibonacci(n):
#     if n < 2 and n >= 0:
#         return 1
#     else:
#         return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# n = int(input("Enter a number to calculate its fibonacci series"))
# result = fibonacci(n)
# print(f"The fibonacci series of {n} is {result}")

# def reversal(n):
#     if n > 0:
#         print(n, end=" ")
#         reversal(n - 1)
#
# n = int(input("Enter a number from where you want a reverse count"))
# reversal(n)

# def reverse_array(A, i, j):
#     if i < j:
#         A[i], A[j] = A[j], A[i]
#         return reverse_array(A, i + 1, j - 1)
#     else:
#         return A
#
# A = [3, 4, 5, 7, 9]
# print(f"Array is equals to {A}")
# result = reverse_array(A, 0, 4)
# print(f"Reversal of array is {result}")

# def recursive_addition(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return n + recursive_addition(n - 1)
#
# n = int(input("Enter a number for recursive addition: "))
# result = recursive_addition(n)
# print(f"Result is: {result}")

# def sumOfRecursion(array):
#     if len(array) == 1:
#         return array[0]
#     else:
#         return array[0] + sumOfRecursion(array[1:])
#
# print(sumOfRecursion([1, 3, 4, 5, 6]))

# def max_array(A, n):
#     if n == 1:
#         return A[0]
#
#     max_element = max_array(A, n - 1)
#     if max_element > A[n - 1]:
#         return max_element
#     else:
#         return A[n - 1]
#
# array = [1, 5, 2, 8]
# n = len(array)
# max_element = max_array(array, n)
# print(max_element)

# def towerOfHanoi(n, start, finish, temporary):
#     if n ==1:
#         print("Move disk 1 from", start, "to", finish)
#         return
#     towerOfHanoi(n-1, start, temporary, finish)
#     print("Move disk", n, "from", start, "to", finish)
#     towerOfHanoi(n-1, temporary, finish, start)
#
# print(towerOfHanoi(3,'A','C','B'))
import sys

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)