#Exercise 6 Compute Pay
# def computepay():
#     hours = input("Enter Hours: ")
#     rate = input("Enter rate: ")
#     try:
#         if int(hours) > 40:
#             Pay = int(hours) * (int(rate) * 1) + (int(hours) -
#                                                   40) / 2 * int(rate)
#             return print('Your Salary is:$', Pay)
#     except:
#         print("Error, please enter numeric input")
#     else:
#         try:
#             Pay = int(hours) * int(rate)
#             return print(
#                 """You did not work for more than 40 hours.
#       Your salary is: $""", Pay)
#         except:
#             print("Error enter number")

# computepay()


#Exercise 7 Compute Grade
def computegrade():
    score = input('Enter a score between 0.0 and 1.0:')
    try:
        score = float(score)
        if score >= 0.9:
            return print('A')
        elif score >= 0.8:
            return print('B')
        elif score >= 0.7:
            return print('C')
        elif score >= 0.6:
            return print('D')
        else:
            return print('F')
    except:
        return print('Bad Entry')


computegrade()
