from os import system, name

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def message() -> str:
    return input("Message: ")