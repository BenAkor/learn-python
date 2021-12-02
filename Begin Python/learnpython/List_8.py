# from typing import List


# nums = [3, 5, 6, 7, 9]

# numlist = list()
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print('Average:', average)


# def chop(t):
#     del t[0]
#     del t[-1]
#     t = t.sort()
#     return t


# def middle(m):
#     return m[1:-2]

# Shakespeare Words


# fhand = open('C:\src\learn-python\Begin Python\learnpython\\romeo.txt')
# unique_list = []
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in unique_list:
#             unique_list.append(word)
#             unique_list.sort()
# print(unique_list)

# Print Maximum and minimum

numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
    maxi = max(numlist)
    minum = min(numlist)
print('Maximum:', maxi)
print('Minimum:', minum)
