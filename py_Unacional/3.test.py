# # read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# # We temporarily assume that the first number
# # is the largest one.
# # We will verify this soon.
# largest_number = number1

# # we check if the second number is larger than current largest_number
# # and update largest_number if needed
# if number2 > largest_number:
#     largest_number = number2

# # we check if the third number is larger than current largest_number
# # and update largest_number if needed
# if number3 > largest_number:
#     largest_number = number3

# # print the result
# print("The largest number is:", largest_number)

# # read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# # check which one of the numbers is the greatest
# # and pass it to the largest_number variable

# largest_number = max(number1, number2, number3)

# # print the result
# print("The largest number is:", largest_number)

# plant = input("Indique el nombre de la planta: ")

# if plant == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# else:
#     if plant == "spathiphyllum":
#         print("No, I want a big Spathiphyllum!")
#     else:
#         print("Spathiphyllum! Not", plant, "!.")

# year = int(input("Enter a year: "))

# if year > 1582:
#     if year % 4 != 0:
#         print("common year")
#     elif year % 100 != 0:
#         print("leap year")
#     elif year % 400 != 0:
#         print("common year")
#     else:
#         print("leap year")
# else:
#     print("Not within the Gregorian calendar period")

# # we will store the current largest number here
# largest_number = -999999999

# # input the first value
# number = int(input("Enter a number or type -1 to stop: "))

# # if the number is not equal to -1, we will continue
# while number != -1:
#     # is number larger than largest_number?
#     if number > largest_number:
#         # yes, update largest_number
#         largest_number = number
#     # input the next number
#     number = int(input("Enter a number or type -1 to stop: "))

# # print the largest number
# print("The largest number is:", largest_number)

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

# odd_numbers = 0
# even_numbers = 0

# # read the first number
# number = int(input("Enter a number or type 0 to stop: "))

# # 0 terminates execution
# while number != 0:
#     # check if the number is odd
#     if number % 2 == 1:
#         # increase the odd_numbers counter
#         odd_numbers += 1
#     else:
#         # increase the even_numbers counter
#         even_numbers += 1
#     # read the next number
#     number = int(input("Enter a number or type 0 to stop: "))

# # print results
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

# odd_numbers = 0
# even_numbers = 0

# # read the first number
# number = int(input("Enter a number or type 0 to stop: "))

# # 0 terminates execution
# while number != 0:
#     # check if the number is odd
#     if number % 2 == 1:
#         # increase the odd_numbers counter
#         odd_numbers += 1
#     else:
#         # increase the even_numbers counter
#         even_numbers += 1
#     # read the next number
#     number = int(input("Enter a number or type 0 to stop: "))

# # print results
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)

# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# for i in range(10):
#     print("The value of i is currently", i)

# for i in range(2, 8):
#     print("The value of i is currently", i)

# largestNumber = -99999999
# counter = 0

# while True:
#     number = int(input("Enter a number or type -1 to end program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largestNumber:
#         largestNumber = number

# if counter != 0:
#     print("The largest number is", largestNumber)
# else:
#     print("You haven't entered any number.")

largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")