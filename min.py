...
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
...
n = int(input("Enter the number of elements: "))
elements = []
for _ in range(n):
    element = int(input())
    elements.append(element)
tuple_data = tuple(elements)
print("Tuple:", tuple_data)
print("Minimum value:", min(tuple_data))
