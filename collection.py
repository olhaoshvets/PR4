#Task 1 Creating set
from conditionOperators import addition

numbers = {'pizza', 'burger', 'soup', 'salad', 'pasta'}
print(numbers)
print(numbers)
print(numbers)
numbers.add('orange')
print(numbers)
numbers.add('pizza')
print(numbers)
numbers.remove('burger')
print(numbers)

# Task 2 Work with set
num1 = {1, 13, 3, 6, 7, 5, 4, 18}
num2 = {14, 3, 7, 11, 12, 9, 1}
num3 = {14, 3, 4, 21, 9, 18, 17, 2}

connect = num1 | num2 | num3
print(connect)

intersection = num1 & num2 & num3
print(intersection)

difference1 = num1.difference(num2)
difference2 = num1.difference(num3)
difference3 = num1 - num2 - num3

print(difference1, difference2, difference3)

symDifference = num1.symmetric_difference(num2)
print(symDifference)

num4 = {3, 4, 9}
checkSubset1 = num2.issubset(num3)
checkSubset2 =num4.issubset(num3)
print(checkSubset1, checkSubset2)

#Task 3 Secret missing
mission = {'шпигунство', 'рятування', 'шахрайство'}
legal = {'шпигунство', 'оберігання'}

dif = mission.difference(legal)
print(dif)
