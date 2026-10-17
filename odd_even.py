# Program: odd_even.py
# Purpose: Loop through a list of 15 numbers and print whether each
#          number is even or odd.

# numbers: list holding the 15 whole numbers to be checked
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# number: loop variable that holds the current item from the list
for number in numbers:
    # A number is even if dividing it by 2 leaves no remainder
    if (number % 2 == 0):
        # str(number) converts the integer to text so it can be
        # joined with the other words in the print statement
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
