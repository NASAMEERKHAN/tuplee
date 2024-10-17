...
Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
...
# Take input for tuple elements in a single line
input_data = input("Enter tuple elements separated by spaces: ")
# Convert the input string into a tuple of integers
tuple_data = tuple(map(int, input_data.split()))

# Take input for the value of x
x = int(input("Enter the value of x: "))

# Count the occurrences of x in the tuple
count_x = tuple_data.count(x)

# Print the tuple and the count of x
print("Tuple:", tuple_data)
print(f"The value {x} occurs {count_x} times in the tuple.")
