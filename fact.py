...
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
...
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

input_data = input("Enter tuple elements separated by spaces: ")
tuple_data = tuple(map(int, input_data.split()))
x = int(input("Enter the value of x: "))

count_x = tuple_data.count(x)

print(f"The value {x} occurs {count_x} times in the tuple.")
print(f"Factorial of {x} is {factorial(x)}.")
