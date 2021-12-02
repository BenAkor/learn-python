# test = dict()
# test['Ben'] = 2
# test['Gift'] = 4

# for (k, v) in test.items():
#     print(k, v)

# Dictionary

# words = dict()
# fhand = open('C:\src\learn-python\Begin Python\learnpython\words.txt')
# for line in fhand:
#     tline = line.split()
#     for sline in tline:
#         if sline not in words:
#             words[sline] = 1
#         else:
#             words[sline] = words[sline] + 1
# print(words)

# given a string and you want to count how many times each letter appears
# word = 'Beginningherehow'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)

# 2
# word = 'brontosarus'
# d = dict()
# for c in word:
#     d[c] = d.get(c, 0) + 1
# print(d)

# Two nested loops
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print(f'File cannot be opened:{fname}')
#     exit()

# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)

# import string
# from typing import Dict
# counts = {'chuck': 1, 'annie': 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:  # to find counts greater than 10
#         print(key, counts[key])
# lst = list(counts.keys())
# print(lst)
# lst.sort()
# for key in lst:
#     print(key, counts[key])

# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print(f'File cannot be opened:{fname}')
#     exit()

# counts = dict()
# for line in fhand:
#     line = line.rstrip()
#     line = line.translate(line.maketrans(
#         '', '', string.punctuation))  # remove punctuations
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)

# Exercise 2 - 9.7

# fname = input('Enter file name:')
# fhand = open(fname)

# week = dict()

# for lines in fhand:
#     if lines.startswith('From '):
#         line = lines.split()
#         line = line[2]
#         if line not in week:
#             week[line] = 1
#         else:
#             week[line] += 1
# print(week)

# Exercise 3 - 9.7

# fname = input("Enter file name here: ")
# fhand = open(fname)

# mailcount = dict()

# for lines in fhand:
#     if lines.startswith('From '):
#         line = lines.split()
#         address = line[1]
#         mailcount[address] = mailcount.get(address, 0) + 1
#         # if address not in mailcount:
#         #     mailcount[address] = 1
#         # else:
#         #     mailcount[address] += 1
# print(mailcount)

# Exercise 4 - 9.7


fname = input("Enter file name here: ")
fhand = open(fname)

mailcount = dict()

for lines in fhand:
    if lines.startswith('From '):
        line = lines.split()
        addresses = line[1]
        mailcount[addresses] = mailcount.get(addresses, 0) + 1

max_key = max(mailcount, key=mailcount.get)
all_values = mailcount.values()
max_value = max(all_values)
print(max_key, max_value)
