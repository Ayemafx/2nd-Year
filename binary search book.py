def binary_search(book_arr, key):
    left = 0
    right = len(book_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if book_arr[mid] == key:
            return mid
        elif book_arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def library(key):
    print(f"Book name is: {key}")
    shelf = binary_search(Algorithm_Book, key)
    if shelf != -1:
        return print(f"Location in Library Algorithm Book shelf: {shelf + 1}")
    shelf = binary_search(Networking_Book, key)
    if shelf != -1:
        return print(f"Location in Library Networking Book shelf: {shelf + 1}")
    shelf = binary_search(Programming_Book, key)
    if shelf != -1:
        return print(f"Location in Library Programming Book shelf: {shelf + 1}")
    return print("Book Not Found")


Algorithm_Book = ['Algorithm Design by Kleinberg & Tardos',
                  'Algorithm for Interviews', 'Algorithm in Nutshell',
                  'Algorithms by Robert Sedgewick & Kevin Wayne',
                  'Data Structures and Algorithms. Aho, Ullman & Hopcroft',
                  'Introduction to Algorithms by Thomas H. Corman',
                  'Introduction to Algorithms: A Creative Approach',
                  'Python Algorithms: Mastering Basic Algorithms in the Python Language',
                  'The Algorithm Design Manual by Steve S. Skiena',
                  'The Design and Analysis of Algorithms']

Networking_Book = ['A Top-Down Approach: Computer Networking',
                   'Business Data Communications and Networking (14th Edition)',
                   'CompTIA Network+ Certification All-in-One Exam Guide',
                   'Computer Networks by Andrew S. Tanenbaum',
                   'High-Performance Browser Networking',
                   'Network Programmability and Automation',
                   'Network Warrior',
                   'Networking All-in-One For Dummies (8th Edition)',
                   'Networking for Systems Administrators (IT Mastery)',
                   'The All-New Switch Book (2nd Edition)']

Programming_Book = ['Clean Code: A Handbook of Agile Software Craftsmanship',
                    'Code Complete: A Practical Handbook of Software Construction',
                    'Design Patterns: Elements of Reusable Object-Oriented Software',
                    'Head First Design Patterns: A Brain-Friendly Guide',
                    'Introduction to Algorithms',
                    'Refactoring: Improving the Design of Existing Code',
                    'Structure and Interpretation of Computer Programs (SICP)',
                    'The Art of Computer Programming, Volumes 1-4',
                    'The Clean Coder: A Code of Conduct for Professional Programmers',
                    'The Pragmatic Programmer']


key = "Network Warrior"
library(key)