#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while num > 1:
        "Happy New year!" if num == 1 else num
        num -= 1
      
print (happy_new_year())

def square_integers(int_list):
    # code goes here!
    # int_list = ([1,2,3,4,5])
    squared_list = [num ** 2 for num in int_list]
    # print (squared_list)
    return squared_list


def fizzbuzz():
    for num in range(1-100):
        return "Fizz" if num % num == 3 else "Buzz" if num % num else "FizzBuzz" if num % num == 3 and num % num == 5 else num
