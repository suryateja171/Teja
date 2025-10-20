stack = []  # Create an empty list to use as a stack

# Push elements into the stack
stack.append(10)     # Add 10 to stack
stack.append(20)     # Add 20 to stack
stack.append(30)     # Add 30 to stack

print("Current Stack:", stack)  # Show the stack

# Pop element from stack
top_element = stack.pop()       # Removes the last element (30)
print("Popped Element:", top_element)

# Check top element using [-1]
print("Top Element Now:", stack[-1])

# Check if stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
