number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


age = int(input("Enter your age: "))
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")


num1 = int(input("enter first number"))
num2 = int(input("enter second number: "))
if num1 > num2:
   print("the larger number is :", num1)
elif num2 > num1:
   print("the larger number is:", num2)
else:
    print("both numbers are equal")



correct_password = "python111"
password = input("Enter your password: ")

if password == correct_password:
    print("Login Successful")
else:
    print("Incorrect Password")
