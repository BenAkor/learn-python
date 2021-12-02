# fhand = open('C:\src\Begin Python\bbox-short.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)

# inp = fhand.read()
# print(len(inp))
# print(inp[:31])

# for line in fhand:
#     if line.startswith('From:'):
#         print(line)

# strip whitespaces
# for line in fhand:
#     line = line.strip()
#     if line.startswith('From:'):
#         print(line)

# fhand = open('C:\src\Begin Python\bbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     # Skip 'uninteresting lines'
#     if not line.startswith('From:'):
#         continue
#     # Process our 'interesting' line
#     print(line)

# fname = input("Enter the file name: ")
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

fname = input("Enter the file name:")
try:
    bhand = open(fname)
except:
    print('Filename is not correct', fname)
    exit()
for bhands in bhand:
    print(bhands.upper())
