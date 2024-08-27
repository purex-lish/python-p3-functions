#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2

# Function calls
greet_programmer()

greet("Arry")

greet_with_default()

result_add = add(5, 3)
print(f"5 + 3 = {result_add}")

result_halve = halve(10)
print(f"10 / 2 = {result_halve}")