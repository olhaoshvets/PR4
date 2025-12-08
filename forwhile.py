#Task 1 While
from itertools import repeat

i = 1

while i < 10:
    print(i ** 2)
    i += 1

#Task 2
repeat = 'yes'

while repeat == 'yes':
    firstNumber = int(input('Enter a number: '))
    operation = input('Enter available operation: +, -, /, *, ** ')
    secondNumber = int(input('Enter a number: '))

    match operation:
        case addition if operation == '+':
            print('The result is', firstNumber + secondNumber)
        case subtraction if operation == '-':
            print('The result is', firstNumber - secondNumber)
        case division if operation == '/':
            print('The result is', firstNumber / secondNumber)
        case multiplication if operation == '*':
            print('The result is', firstNumber * secondNumber)
        case exponentiation if operation == '**':
            print('The result is', firstNumber ** secondNumber)
        case _:
            print('Invalid operation')

    repeat = input('Do you want to continue? yes/no ').lower().strip()

#Task 3
i = 0
while i < 10:
    i += 1
    if  i == 5 or i == 7:
        continue
    print(i)

#Task 4
import random
num =  random.randint(1,20)
userInput = int(input('Guess a number from 1 to 20: '))
retries = 1

while num != userInput:
    if num > userInput:
        retries += 1
        print('Guessed number is bigger')
    elif num < userInput:
        retries += 1
        print('Guessed number is smaller')

    userInput = int(input('Try to guess again: '))

print('You guessed from the', retries, 'attempt')

#Task 5
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

#Task 1 For
for i in range(7, 0, -1):
    print('*' * i)

#Task 2
text = 'bananas are amazing fruits'
letters = []
countA = 0
length = len(text)

for i in range(length):
    if text[i] == 'a':
        countA += 1
        letters.append(text[i])
    elif text [i] != ' ':
        letters.append(text[i])

print(letters, '"a" meets in text', countA, 'times')

#Task 3
our_list = [1, 5, 8, -5, 34, 9, 10]
sum = 0
evenCount = 0

for i in range(len(our_list)):
    sum += our_list[i]
    if our_list[i] % 2 == 0:
        evenCount += 1

print('Sum of array elements is', sum, 'Even numbers count is', evenCount)

#Task 4
products = {
    "Молоко": 45,
    "Хліб": 28,
    "Сир": 160,
    "Кава": 230,
    "Цукор": 52,
    "Масло": 185,
    "Шоколад": 95,
    "Печиво": 120,
    "Сік": 75,
    "Чай": 150
}
products_updated = products.copy()
sum = 0

for i in products:
    if (products.get(i)) > 100:
        sum += products.get(i)
    else:
        products_updated.pop(i)

print(products_updated, 'The total:', sum, 'UAH')

#Task 5
our_list = [1, 5, 8, -5, 34, 9, 10]

for i in our_list:
	if i > 10:
		continue
	print(f"індекс {our_list.index(i)} = {i}")
