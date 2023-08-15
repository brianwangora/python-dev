'''
Determining whether a given number is prime
-----------------------------------------
'''

# Input
print('This program wishes to determine if a number is prime number')

def prime_number(number):
    c = 0
    for i in range(2, number):
        if number % i == 0:
            c = c + 1
    return c


try:
    number = int(input("Enter a number: "))
    if prime_number(number) == 0:  
        print('True')
    else: 
        print('False')
except ValueError as err:
    print('Kindly enter a number.')
    print(err)
        

