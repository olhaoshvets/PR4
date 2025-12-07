#Task 1 Creating set

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

mission = mission.intersection(legal)
print(mission)

# dif = mission.difference(legal)
# for illegal in dif:
#     if illegal in mission:
#         mission.remove(illegal)

#Task 4 Creating tuple
numbers = (1, 2, 3, 4, 5)
print(numbers[1])
print(numbers[0], numbers[-1])
print(numbers[:2])
print(len(numbers))

#Task 5 Changing tuple
numbers = (1, 2, 3, 4, 5, -5, 12, 5, 42, 34)

numbers = list(numbers)
numbers.append(-56)
numbers = tuple(numbers)
print(numbers)

numbers = list(numbers)
numbers.remove(5)
numbers = tuple(numbers)
print(numbers)

#Task 6 Join & unpacking
fruits1 = ('apple', 'orange', 'banana', 'pineapple', 'cgerrys')
fruits2 = ('mango', 'orange', 'lemon', '”', 'pear')
num = (1, -6, 23, 45)

fruits3 = fruits1 + fruits2
print(fruits3)

num1 = num * 3
print(num1)

(first, *rest, last1, last2) = fruits3

print(first)
print(last1, last2)
print(rest)