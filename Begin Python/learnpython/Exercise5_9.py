#Exercise 5 Iterations
#Exercise 1
# count = 0
# total = 0
# average = 0
# while True:
#     line = input('Enter a number or done when finished:')
#     try:
#         count = count + 1
#         total = total + int(line)
#         average = total / count
#         print(line, total)
#     except:
#         if line == 'done':
#             break
# print('Count:', count, 'Total:', total, 'Average:', average)

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

smallest = None
largest = None
# while True:
numbers = input()
for number in numbers:
    try:
        if smallest is None or int(number) < smallest:
            smallest = int(number)
            print('Loop:', number, smallest)
        if largest is None or int(number) > largest:
            largest = int(number)
            print('Loop:', number, largest)
    except:
        if numbers == 'done':
            break
        print('Smallest:', smallest, 'Largest:', largest)
print('Smallest:', smallest, 'Largest:', largest)
