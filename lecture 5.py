# Num = (1,4,9,16,25,36,49,64,81,100)
# X = int(input("Enter a number: "))
# i=0
# while i < len(Num):
#     if Num[i] == X:
#         print("Number found at index", i)
#         break
#     i+=1
# else:
#     print("Number not found")

# Num = (1,4,9,16,25,36,49,64,81,100)
# X = int(input("Enter a number: "))
# for val in Num :
#     if val == X:
#         print("Number found at index", Num.index(val))
#         break
#     print(val)


# Number = int(input("Enter a number: "))
# Int = range (Number,Number*10+1,Number)
# for val in Int:
#     print(val)

# Num = int(input("Enter a number: "))
# Factorial = 1
# for i in range(1, Num+1):
#     Factorial *= i
# print("Factorial of", Num, "is", Factorial)

# def average(a,b,c):
#     Avg= (a+b+c) / 3
#     return Avg

# print(average(1,14,52))

# def legth (str):
#     count = 0
#     for char in str:
#         count += 1
#     return count

# Str = input("Enter a string: ")
# print("Length of the string is:", legth(Str))

# cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# def element_at_index(cities):
#     for i in cities:
#         print(i, end=" ")
# element_at_index(cities)
# n = int(input("Enter a number: "))
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact
# print("Factorial of", n, "is", factorial(n))

# print(factorial(5))

# def dollar_to_inr(dollar):
#     inr = dollar * 93
#     print(dollar, "Dollars=", inr, "INR")
#     return inr

# dollar_to_inr(1000)

# def odd_even(Num):
#     if Num % 2 == 0:
#         print(Num, "is an even number.")
#     elif Num % 2 != 0:
#         print(Num, "is an odd number.")
#     else:
#         print("Enter a valid Inteager.")
# Num = int(input("Enter a number: "))
# odd_even(Num)   


# def sum(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
# n = int(input("Enter a number: "))
# print("Sum of first", n, "natural numbers is", sum(n))


# from operator import index


# def element(list,index):
#     if index == len(list):
#         return "Index out of range"
#     print(list[index])
#     element(list, index+1)

# cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# element(cities, 0)

import random

def play_game():
    print("🎮 Welcome to Number Guessing Game!")

    # Difficulty selection
    print("\nChoose Difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    choice = int(input("Enter choice (1/2/3): "))

    if choice == 1:
        number = random.randint(1, 50)
        attempts = 10
    elif choice == 2:
        number = random.randint(1, 100)
        attempts = 7
    else:
        number = random.randint(1, 200)
        attempts = 5

    score = 0

    while attempts > 0:
        guess = int(input("\nEnter your guess: "))
        attempts -= 1

        if guess == number:
            print("🎉 Correct! You win!")
            score = attempts * 10
            break
        elif guess > number:
            print("📉 Too high!")
        else:
            print("📈 Too low!")

        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"💀 Game Over! The number was {number}")

    print(f"🏆 Your Score: {score}")

# Run game
play_game()