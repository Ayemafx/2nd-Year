def is_palindrome_using_stack(input_string):
    stack = []
    for char in input_string:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    if input_string == reversed_string:
        return (f"{input_string} is a palindrome")
    else:
        return (f"{input_string} is not a palindrome")

print(is_palindrome_using_stack("racecar"))  # Output: True
print(is_palindrome_using_stack("hello"))    # Output: False

from collections import deque


def is_palindrome(string):
    # create a deque and add each character of the string to it
    char_deque = deque()
    for char in string:
        char_deque.append(char)

    # compare characters from both ends of the deque until there are no more left to compare
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return (f"{string} is not a palindrome")

    return (f"{string} is a palindrome")


# test the function with some example strings
print(is_palindrome('racecar'))  # True
print(is_palindrome('hello'))  # False
