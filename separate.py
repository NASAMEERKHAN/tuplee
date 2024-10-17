...
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
...
# Function to get tuple elements and return the sum
def get_tuple_sum():
    # Take the number of elements in the tuple from the user
    n = int(input("Enter the number of elements: "))
    
    # Initialize an empty list to store the elements
    elements = []
    
    # Loop to get 'n' elements from the user
    for _ in range(n):
        element = int(input())  # Take each element as input
        elements.append(element)  # Append the element to the list
    
    # Convert the list to a tuple
    tuple_data = tuple(elements)
    
    # Calculate and print the sum of the tuple elements
    print("Tuple:", tuple_data)
    print("Sum of elements:", sum(tuple_data))

# Call the function
get_tuple_sum()
