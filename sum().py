...
 Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
...
input_data = input("Enter tuple elements separated by spaces: ")
tuple_data = tuple(map(int, input_data.split()))
total = 0
for num in tuple_data:
    total += num
print("Tuple:", tuple_data)
print("Sum of elements:", total)
