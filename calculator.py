
from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Functions
operations = {
    '+': add,
    '-': subract,
    '*': multiply,
    '/': divide
}
def calculator():
    print(logo)
    still_running = True

    num1 = float(input('What is the first number: '))
    while still_running == True:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What is the next number: '))
        answer = operation_symbol(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f'Type y to continue calculating with {answer}, or type n to start a new calculation. ') == 'y':
            num1 = answer
        else:
            still_running = False
            calculator()