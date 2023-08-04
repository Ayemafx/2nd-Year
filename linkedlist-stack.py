class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        dequeued_node.next = None
        return dequeued_node.data

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data


# Creating a new stack object
my_stack = Stack()

# Adding elements to the stack
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

# Peeking the top element of the stack
print(my_stack.peek())  # Output: 15

# Removing the top element from the stack
my_stack.pop()

# Creating a new queue object
my_queue = Queue()

# Adding elements to the queue
my_queue.enqueue(5)
my_queue.enqueue(10)
my_queue.enqueue(15)

# Peeking the front element of the queue
print(my_queue.peek())  # Output: 5

# Removing the front element from the queue
my_queue.dequeue()
