from collections import deque

# deque is short term ab out double-ended queue. It's in short data structure, which is working like list, but with additional fuctionality
#  Its naturally better choice to create stack than regular list

# using deque
my_deque = deque()

my_deque.append(1)  # Dodanie elementu 1 na koniec kolejki
my_deque.appendleft(2)  # Dodanie elementu 2 na początek kolejki
print(my_deque)  # Output: deque([2, 1])

item = my_deque.pop()  # Usunięcie i zwrócenie ostatniego elementu kolejki
print(item)  # Output: 1

item = my_deque.popleft()  # Usunięcie i zwrócenie pierwszego elementu kolejki
print(item)  # Output: 2

#using regular list as a stack

stack = []
stack.append("element1")
stack.append("element2")
stack.append("element3")

print(stack)

#poping elements from stack using pop()
#LIFO order

print("Elements moved from stack")
print("stack.pop()")
print("stack.pop()")

#another metod to define stack


class Node:
    def __init__(self,what):

    

