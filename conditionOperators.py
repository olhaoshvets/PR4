#Task 1
number = int(input('Enter any number: '))
if number > 0:
    print("Positive")

name = input('Enter your name: ')
if name == 'Olha':
    print('Success!')

#Task 2
evenOdd = int(input('Enter any number'))
if evenOdd % 2 == 0:
    print('Even')
else:
    print('Odd')

#Task 3
password = input('Enter your password:')
if password == 'qWerTy123!':
    print('Access allowed!')
else:
    print('Access denied!')

#Task 4
text = input('Enter any text:').lower().strip()

if text.find('a') > -1:
    print('Let you in')
else:
    print('You shall not pass')

#Task 5
week_day = input('Enter the week day:').lower().strip()

if week_day == 'monday':
    print('Monday brings you new experience')
elif week_day =='tuesday':
    print('Tuesday is better than Monday, but still not Friday')
elif week_day =='wednesday':
    print('Wednesday going to be better than a TV-series character')
elif week_day == 'thursday':
    print('Thursday is a small Friday')
elif week_day == 'friday':
    print('This day cannot be bad')
elif week_day == 'saturday':
    print('Its a nice day to go for a walk')
elif week_day == 'sunday':
    print('Shine bring like diamond')
else:
    print('I dont recognize this week day, please try again')

# Task 6
password = input('Enter your password: ')

if len(password) < 4:
    print('Your password is too short')
elif len(password) > 10:
    print('Your password is too long')
else:
    print('The password is accepted')

# Task 7
age = int(input('Enter your age: '))

result = 'Adult' if age > 18 else 'Kid'
print(result)

#Task 8
month = int(input('Enter month number from 1 to 12: '))

match month:
    case 1:
        print('January')
    case 2:
        print('February')
    case 3:
        print('March')
    case 4:
        print('April')
    case 5:
        print('May')
    case 6:
        print('June')
    case 7:
        print('July')
    case 8:
        print('August')
    case 9:
        print('September')
    case 10:
        print('October')
    case 11:
        print('November')
    case 12:
        print('December')
    case month if month < 1 or month > 12:
        print('Please enter the number from the range')

#Task 9
score = input('Enter a score from A to F: ').lower()

match score:
    case A if score == 'a':
        print('Your score is 5')
    case B if score == 'b':
        print('Your score is 4')
    case C if score == 'c':
        print('Your score is 3')
    case D if score == 'd':
        print('Your score is 2')
    case F if score == 'f':
        print('Your score is 1')
    case _:
        print('No match')

# Task 10
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

#Task 11
password = input('Enter your password: ')
length = len(password)

if length < 8:
    print('Your password is too short')
elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print('Your password is safe')
elif password.isalpha():
    print('Add number to your password')
elif password.isdigit():
    print('Add character to your password')
else:
    print('Invalid password')
