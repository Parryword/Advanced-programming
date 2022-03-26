# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('What is your name?')
    x = input()
    print('Hello ' + x)
    print('What is your student ID?')
    y = input()
    print('Your ID is ' + y)

    print()

    print('Enter number1')
    number1 = input()
    print('Enter number2')
    number2 = input()

    sum = int(number1) + int(number2)
    diff = int(number1) - int(number2)
    prod = int(number1) * int(number2)

    print('sum: ' + str(sum))
    print('diff: ' + str(diff))
    print('prod: ' + str(prod))

    print('\n*\n**\n***')
    
    print('Press any to exit')
    input()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
