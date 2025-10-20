# class MathOps:
#     def __init__(self):
#         print("MathOps object created!")

#     def add(self, a=0, b=0, c=0):
#         result = a + b + c
#         print(f"Sum of values: {a} + {b} + {c} = {result}")
#         return result
    

#     math = MathOps()


#     math.add(10)
#     math.add(10,20)
#     math.add(10,20,30)    






# class Animal:
#         def __init__(self):
#             print("Animal is created.")
#         def __init__("Animal makes a sound.")
# class Dog:
#         def __init__(self):
#             super().__init__()
#             print("Dog is created.")
#         def speak(self):
#         print("Dog barks.")   

# Animal = Animal()
# animal.speak() 
        






class Node:
    def __init__(self, data):
        self.data = data  # stores value
        self.next = None  # points to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # first node

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:  # empty list
            self.head = new_node
        else:
            current = self.head
            while current.next:  # go to last node
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

# Test the singly linked list
sll = SinglyLinkedList()
sll.add_node(10)
sll.add_node(20)
sll.add_node(30)
sll.display()






class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

# Test
sll = SinglyLinkedList()
sll.add_node(10)
sll.add_node(20)
sll.add_node(30)
sll.display()









class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Create the list and add values
sll = SinglyLinkedList()
sll.add_node(10)
sll.add_node(20)
sll.add_node(30)
sll.add_node(40)
sll.display()






class Node:
    def __init__(self, data):
        self.data = data      # stores the value
        self.prev = None      # points to the previous node
        self.next = None      # points to the next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None      # the first node (start of the list)

    def add_node(self, data):
        new_node = Node(data)  # create a new node with given value

        if self.head is None:  # if the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:     # go to the last node
                current = current.next
            current.next = new_node # link the new node at the end
            new_node.prev = current # link back to previous node

    def display_forward(self):
        current = self.head
        print("Forward: ", end="")
        while current:
            print(current.data, end=" ⇄ ")
            current = current.next
        print("None")






