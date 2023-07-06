from collections import deque

# deque is short term ab out double-ended queue. It's in short data structure, which is working like list, but with additional fuctionality
#  

my_deque = deque()

my_deque.append(1)  # Dodanie elementu 1 na koniec kolejki
my_deque.appendleft(2)  # Dodanie elementu 2 na początek kolejki
print(my_deque)  # Output: deque([2, 1])

item = my_deque.pop()  # Usunięcie i zwrócenie ostatniego elementu kolejki
print(item)  # Output: 1

item = my_deque.popleft()  # Usunięcie i zwrócenie pierwszego elementu kolejki
print(item)  # Output: 2
