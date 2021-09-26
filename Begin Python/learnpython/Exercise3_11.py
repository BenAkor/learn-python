#Exercise 1
# hours = input("Enter Hours: ")
# rate = input("Enter rate: ")
# if int(hours) > 40:
#     Pay = int(hours) * (int(rate) * 1) + (int(hours) - 40) / 2 * int(rate)
#     print("This is your salary: $", Pay)
# else:
#     Pay = int(hours) * int(rate)
#     print("""You did not work for more than 40.
#     Your salary is: $""", Pay)

#Exercise 2
# hours = input("Enter Hours: ")
# rate = input("Enter rate: ")
# try:
#     if int(hours) > 40:
#         Pay = int(hours) * (int(rate) * 1.5)
#         print("This is your salary: $", Pay)
# except:
#     print("Error, please enter numeric input")
# else:
#     try:
#         Pay = int(hours) * int(rate)
#         print("""You did not work for more than 40.
#     Your salary is: $""", Pay)
#     except:
#         print("Error enter number")

score = input('Enter a score between 0.0 and 1.0:')
score = float(score)
try:
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')
except:
    print('Bad entry')
