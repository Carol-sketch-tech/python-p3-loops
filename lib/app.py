# loops
# loops for and while looops.

# bsic syntax for while loop in python 
 
i = 0
while i < 5:
    print ("Looping!")
    i += 1


z = 10
while z <  100:
    print ("Hello Caroline Wanjiru")
    z += 1    

    # /Looping with for 
# pythons  for loop simple syntax 

for i in range(10):
    print("Looping!")
    print(f"i is :{i}")

# when writing a for loop in python, the looop can proceed through any iterable object type.
# these iretables obejct types are lists,tuple,set and dict ans well as string and range objects.
# range objects are especially useful in the for construct because they generate an ordered sequence of ints from 0
# through a number of your choosing
# note that the for loop in python automatically proceeds tot he ext element of the iterable object in its constructor,
#  there is no need to specify thatt the loop is stopping at a certain point or increaising after each iteration.

# List Comprehensions.

# ->  Question.  you have measured the height of each player in the NCAA but now yo have all of the data in front of you.
# you can see that you ve made a horiible mistake . you have measured all the heights in furlongs.
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
inch_heights = list()
for height in player_heights:
    inch_height = height * 7920
    inch_heights.append(inch_height)
print(inch_heights)    
    # with he above code you have written fourlines of code and yet we require only a simple line of code to solve this issue.

# list comprehension allows us to transform sequences of data in a single line.as follows 
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
wanted_heights_in_inch = {height * 7920 for height in player_heights} 
print(wanted_heights_in_inch)


player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
expected_heights = [height * 7920 for height in player_heights]
print(expected_heights)



# List compressions are very poerful tools buthtere are jobs that a for loop is better suited for.
# there are two main factors to keep in mind when choosing between the two:
#   1. List compressions should only be used for loops where the output is an iterble object such as a list or a set.
#    2. for loops seprate steps into different lines, which is how human eeyes expects to see instructions. list compressions are restricted 
# t a single line and can be difficult for other humans to understand.


def happy_new_year():
    num = 10
    while num > 1:
        for num in range(10-1):
            return num if num <= 10 and >= 2 else "Happy New Year!"
       
print(happy_new_year())        