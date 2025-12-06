#Task 1
nums = [1, 5, 5, -4, 12, 42, 2]
print(nums)

nums.append(8)
print(nums)

nums.remove(5)
print(nums)

index = nums.index(12)
nums[index] = -12
print(nums)

nums.insert(4, -8)
print(nums)

nums.reverse()
print(nums)

nums.clear()
print(nums)

#Task 2
menu = ['pizza', 'burger', 'soup', 'salad']

menu.append('pasta')
menu.remove('soup')
print(menu)

#Task 3
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in nums:
    if num % 2 != 0:
        nums.remove(num)
print(nums)

#Task 4
letters = ['a', 'b', 'c', 'd', 'e', 'f']

first3Letters = letters[0:3]
print(first3Letters)

specificLetters = letters[2:4]
print(specificLetters)

eachThirdLetter = []
for i in range(0, len(letters), 3):
    eachThirdLetter.append(letters[i])
print(eachThirdLetter)

#Task 5
test_list = [1, -5, True, 'banana', 'car', 3.124, -5, '-5']

count = test_list.count('-5') + test_list.count(-5)
print('-5 meets', count, 'times in the list')

length = len(test_list)
print(length)

if 'banana' in test_list:
    print('Yes, banana is in the list')

#Task 6
num1 = [1, 5, -4, 10, 2, 2, 3.4, -4]
num2 = [3, -6, -7, -89, 90, 2]

num1.extend(num2)
print(num1)

num1.sort(reverse=True)
print(num1)

num1.sort(reverse= False)
print(num1)
