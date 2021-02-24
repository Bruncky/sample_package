from termcolor import colored

def try_me(*args):
    if not args:
        print("Hi there! My name is Jonathan. What's your name?")
        print(colored('psst...you can tell me your name by calling the same method again with your name as a parameter!', 'grey'))
    else:
        print(f'Hi there, {args[0]}! How are you doing?')
        print(colored('Ok, no check the README to see what else I can do!', 'grey'))