...
 Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
...

input_data = input("Enter tuple elements separated by spaces: ")
tuple_data = tuple(map(int, input_data.split()))
print("Tuple:", tuple_data)
print("Number of elements:", len(tuple_data))
