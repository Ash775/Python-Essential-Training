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
