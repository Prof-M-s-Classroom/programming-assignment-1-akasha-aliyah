from temperature import Temperature

class Node:     # node class to be used in the linked list implementation of the stack

    def __init__(self, data):       # initialize node with data and pointer to next node
        self.data = data
        self.prev = None

class CircularStack: # circular stack class using a linked list with a maximum of 5 elements
    def __init__(self):     # initialize stack with an empty state
        self.top = None
        self.length = 0
        self.max_size = 5

    def push(self, temperature, humidity):      # add a new Temperature object to the stack, replacing the oldest entry if full
        new_node = Node(Temperature(temperature, humidity))
        if self.length == 0:
            self.top = new_node
            self.length += 1
        else:
            new_node.prev = self.top
            self.top = new_node
            self.length += 1

        if self.length > self.max_size:
            self.pop()

    def pop(self):      # remove the oldest entry from the stack
        temp = None
        if self.length == 0:
            print("Stack is empty.")
            return None
        elif self.length == 1:
            self.top = None
        else:
            temp = self.top
            while temp.prev and temp.prev.prev:     # while temp.prev != None, move until second-to-last value
                temp = temp.prev
            temp.prev = None
        self.length -= 1
        return temp

    def peek(self):     # return the most recent temperature entry without removing it
        if self.length == 0:
            print("Stack is empty.")
            return None
        else:
            print(self.top.data)
            return self.top.data

    def print_stack(self):      # print all stored readings in order from oldest to newest
        if self.length == 0:
            print("Stack is empty.")
        temp = self.top
        stack = []
        while temp:
            stack.append(temp.data)
            temp = temp.prev
        for data in reversed(stack):
            print(data)

    def is_empty(self):     # return True if the stack is empty, otherwise False
        return self.length == 0

"""
# Example Stack
test_stack = CircularStack()
test_stack.push(97,24)
test_stack.push(10,11)
test_stack.push(8,3)
test_stack.push(5,21)
test_stack.push(17,19)
test_stack.print_stack()

test_stack.push(47,43)
print("")
test_stack.print_stack()

print("")
test_stack.pop()
test_stack.print_stack()

"""