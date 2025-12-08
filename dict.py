#Task 1 Creating dictionary
about_me = {
    'name': '',
    'surname': '',
    'age': '',
    'dob': '',
    'city': ''
}

about_me['name'] = 'Olha'
about_me['surname'] = 'Shvets'
about_me ['age'] = '27'
about_me['dob'] = '01.04.98'
about_me['city'] = 'Kharkiv'

key_list = about_me.keys()
value_list = about_me.values()
item_list = about_me.items()

print(key_list)
print(value_list)
print(item_list)

#Task 2 Items
prices = {
    'apple': 50,
    'banana': 20,
    'cherry': 75
}

max = max(prices.keys())
print(max)

#Task 3 Students list
students = {
    'James' : 3,
    'Odin' : 5,
    'Sarah' : 5,
    'John' : 4,
    'Noah' : 2
}

average = sum(students.values()) / 5
print(average)

#Task 4 Magic translation
words = {
    'apple': 'яблуко',
    'cow': 'корова',
    'orange': 'апельсин',
    'hello': 'привіт',
    'Monday': 'Понеділок',
    'dog': 'пес'
}

userInput = input('Enter the word: ')
wordsList = words.keys()
translateList = words.values()

if userInput in wordsList:
    print(words.get(userInput))
else:
    print('unknown')

#Task 5 Check the key
user = {
    'login': 'admin',
    'password': '1234587',
}

if 'email' in user:
    print(user.get('email'))
else:
    user['email'] = 'admin@gmail.com'
print(user)

#Task 6 Check the code
user = {
'name': 'Petro',
'age': 12
}
# user.add('city':'Kyiv')
# print(user)

user.update({"name":"Anna", "age": 21})
user["city"] = 'Kyiv'
print(user)