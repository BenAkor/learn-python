fruit = 'Banana'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1

# Exercise 1
# index = -1
# while index > -(len(fruit)) - 1:
#     letter = fruit[index]
#     print(letter)
#     index = index - 1

# for char in fruit:
#     print(char)

# s = fruit[:3]
# print(s)

# def count():
#     word = input('Enter a sentence:')
#     letter = input('Letter to find:')
#     count = 0
#     for test in word:
#         if test == letter:
#             count = count + 1
#     print(count)

# count()

#Exercise 6.14
str = 'X-DSPAM-Confidence:0.8475'
test = str.find(':')

ntest = str.find(' ', test)

ptest = str[test + 1:]
stest = float(ptest)
print(stest)