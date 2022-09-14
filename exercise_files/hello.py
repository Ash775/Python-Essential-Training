import sys

from termcolor import colored

print(colored("Hello, World!", "red"))
print(colored("Hello, World!", "green"))
print(colored("Hello, World!", "yellow"))
print(colored("Hello, World!", "blue"))
print(colored("Hello, World!", "magenta"))
print(colored("Hello, World!", "cyan"))

my_Dictionary = {
    'Apple': colored('A red frutit', 'red'),
    'Bear' : 'A scary animal',

}

print(my_Dictionary['Apple'])

my_List = [
    [1],[2, 'boy'], [3, 34, 'lol']
]

print(my_List)
print(len(my_List))

my_Set = {1,2,2,3,4,5,5,5}
print(my_Set)
print(type(my_Set))
print(len(my_Set))

my_List.append(6)
print(my_List)

my_Tuple = (1,2,3,4,5)
print(my_Tuple)

a= [1,2,3,4,5]
for items in a:
    print (items)

a = 0
while a <= 5:
    print (a)
    a = a + 1

def sum (val1, val2):
    return val1 + val2
print(sum(5000,4))

x = [1,2,3,4,5]

def appendnumber(number):
    number.append(6)

appendnumber(x)
print(x)


