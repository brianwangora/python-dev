'''
Displaying the numbers between a given range
-----------------------------------------------------------
'''

# Input the numbers
a = int(input('Enter a number a: '))
b = int(input('Enter a number b: '))


def integers(a,b):
    numbers = []
    for value in range(a, b + 1):
        numbers.append(value)
    if numbers == []:
        print('Make sure that a is less than b.')
    else:
        print(numbers)

integers(a,b)