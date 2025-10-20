# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None  
#         self.next = None  


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next: 
#             temp = temp.next
#         temp.next = new_node
#         new_node.prev = temp  


#     def display_forward(self):
#         print("Forward Traversal:")
#         temp = self.head
#         while temp:
#             print(temp.data, end=" <-> ")
#             last = temp
#             temp = temp.next
#         print("None")

#     def display_backward(self):
#         print("Backward Traversal:")
#         temp = self.head
#         if not temp:
#             return
        
#         while temp.next:
#             temp = temp.next
        
#         while temp:
#             print(temp.data, end=" <-> ")
#             temp = temp.prev
#         print("None")


# dll = DoublyLinkedList()
# dll.insert(10)
# dll.insert(20)
# dll.insert(30)

# dll.display_forward()   
# dll.display_backward() 
       

print("10 <-> 20 <-> 30 <-> None")
print("30 <-> 20 <-> 10 <-> None")