# import Friend
# print('Hello Benaiah')


# def Hello():
#     print("This is a function")

# Hello()

# name = input("Enter your name : ")

# print("Hello", name)

# age = input("Enter your age : ")
# age = int(age)

# print("I am", age, "years old")

# x = 8
# y = "Ben"

# print(type(x))
# print(type(y))

# x = ('Banana', 'Plantain', 'Apple')  # Tuple
# print(x)
# x = ["Butter", "Milk", "sugar"]  # List
# print(x)
# x = {"Test": "You",
#      "Age": 67,
#      "Song": "My Song"}  # map key : Value
# print(x)
# x = True
# print(x)

# x = range(10)
# print(x)

# import random
# test = """ This is
# a multiline string that we are using
# """

# test_y = ''' This is also
# a multiline string '''

# print(test, test_y)

# test_x = "Gift my love"

# print(test_x[2])
# print(test_x[0:4])

# print(len(test_y))

# # looping

# for x in test_y:
#     print(x)

# print("This" in test_y)
# print("This" not in test_x)

# # numbers
# print(random.random())
# print(random.randrange(1, 290))
# print(random.randint(10, 50))

# Boolean

# print(10 > 2)
# print(bool("Test"))
# print(bool(10))
# print("hello" in "Hello World")

# sub = ["python", "java", "ruby"]
# print(sub)
# print(sub[1])

# x = 30
# y = 10

# if x > y:
#     print(x, "is greater")
# else:
#     print(y, "is greater")

# for x in range(1, 10):
#     print(x)

# # Function


# def hello():
#     print("Good Day")


# def sum(x, y):
#     # x = 10
#     # y = 25
#     c = x+y
#     return c


# x = input("Enter number for x : ")
# y = input("Enter number for y : ")

# print(sum(int(x), int(y)))

class Car:
    x = 10

    def carFunc(self):
        print("I am inside car class")


car1 = Car()
print(car1.x)
