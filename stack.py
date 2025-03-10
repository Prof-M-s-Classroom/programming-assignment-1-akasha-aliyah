from distance import Distance

class Node:     # node class to be used in the linked list implementation of the stack
    def __init__(self, data):       # initialize node with data and pointer to next node
        self.data = data
        self.next = None

class CircularStack: # circular stack class using a linked list with a maximum of 5 elements
    def __init__(self):     # initialize stack with an empty state
        self.top = None     # newest entry
        self.rear = None    # oldest entry
        self.size = 0
        self.max_size = 5

    def push(self, distance):      # add a new distance object to the stack, replacing the oldest entry if full
        new_node = Node(Distance(distance))
        if self.size == 0:
            self.top = new_node
            self.rear = new_node
            new_node.next = new_node
        else:
            self.top.next = new_node
            self.top = new_node
            self.top.next = self.rear

        if self.size < self.max_size:
            self.size += 1
        else:
            self.rear = self.rear.next      # move rear to the second-oldest entry
            self.top.next = self.rear

    def pop(self):      # remove the oldest entry from the stack
        if self.size == 0:
            print("Stack is empty.")
            return None
        elif self.size == 1:
            removed = self.rear.data
            self.top = None
            self.rear = None
            self.size = 0
        else:
            removed = self.rear.data
            self.rear = self.rear.next      # move rear forward
            self.top.next = self.rear       # maintain circular link
            self.size -= 1
        return removed

    def peek(self):     # return the most recent temperature entry without removing it
        if self.size == 0:
            print("Stack is empty.")
            return None
        return self.top.data

    def print_stack(self):      # print all stored readings in order from oldest to newest
        if self.size == 0:
            print("Stack is empty.")
            return
        temp = self.rear
        count = 0
        while count < self.size:
            print(temp.data)
            temp = temp.next
            count += 1

    def is_empty(self):     # return True if the stack is empty, otherwise False
        return self.size == 0

"""
# Example Stack
test_stack = CircularStack()
test_stack.push(24)
test_stack.push(11)
test_stack.push(3)
test_stack.push(21)
test_stack.push(19)
test_stack.print_stack()

test_stack.push(43)
print("")
test_stack.print_stack()

print("")
test_stack.pop()
test_stack.print_stack()
"""