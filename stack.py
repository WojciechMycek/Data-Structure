from collections import deque

# deque is short term ab out double-ended queue. It's in short data structure, which is working like list, but with additional fuctionality
#  Its naturally better choice to create stack than regular list

# using deque
my_deque = deque()

my_deque.append(1) 
my_deque.appendleft(2) 
print(my_deque) 

item = my_deque.pop() 
print(item)  
item = my_deque.popleft()  


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

#lists

my_list = [1, 2, 3, 4, 5]


my_list.append(6)


print("Lista po dodaniu elementu:", my_list)


print("Pierwszy element:", my_list[0])
print("Trzeci element:", my_list[2])


my_list[1] = 10
print("Lista po zmianie elementu:", my_list)

del my_list[2]
print("Lista po usunięciu elementu:", my_list)

my_list.insert(2, 7)
print("Lista po wstawieniu elementu:", my_list)

my_list.sort()
print("Posortowana lista:", my_list)

my_list.reverse()
print("Odwrócona lista:", my_list)

my_list.pop()
print("Lista po usunięciu ostatniego elementu:", my_list)

print("Długość listy:", len(my_list))

#tuple

my_tuple = (1, 2, 3, 4, 5)

print("Pierwszy element:", my_tuple[0])
print("Trzeci element:", my_tuple[2])

print("Długość tupli:", len(my_tuple))

new_tuple = my_tuple + (6, 7, 8)
print("Połączona tupla:", new_tuple)

repeated_tuple = my_tuple * 3
print("Powtórzona tupla:", repeated_tuple)


#sets

my_set = {1, 2, 3, 4, 5}

my_set.add(6)

print("Zbiór:", my_set)

my_set.remove(3)
print("Zbiór po usunięciu elementu:", my_set)

print("Czy 2 istnieje w zbiorze?", 2 in my_set)
print("Czy 7 istnieje w zbiorze?", 7 in my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print("Suma zbiorów:", union_set)

intersection_set = set1.intersection(set2)
print("Przekrój zbiorów:", intersection_set)

difference_set = set1.difference(set2)
print("Różnica zbiorów (set1 - set2):", difference_set)

subset = {1, 2}
print("Czy {1, 2} jest podzbiorem set1?", subset.issubset(set1))

#dictionary:

my_dict = {'jabłko': 5, 'banan': 3, 'gruszka': 2}


print("Liczba jabłek:", my_dict['jabłko'])
print("Liczba bananów:", my_dict['banan'])


my_dict['gruszka'] = 4
print("Słownik po zmianie wartości:", my_dict)


my_dict['pomarańcza'] = 6
print("Słownik po dodaniu nowej pary klucz-wartość:", my_dict)


del my_dict['jabłko']
print("Słownik po usunięciu pary klucz-wartość:", my_dict)


print("Klucze słownika:", my_dict.keys())


print("Wartości słownika:", my_dict.values())

print("Pary klucz-wartość słownika:", my_dict.items())
