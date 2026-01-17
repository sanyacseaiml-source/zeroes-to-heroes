print("1. Even or Odd")
print("2. Voting Eligibility")
print("3. Largest of Two Numbers")
print("4. Login Check")

choice = int(input("Enter choice: "))

if choice == 1:
    n = int(input("Enter number: "))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif choice == 2:
    age = int(input("Enter age: "))
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a > b:
        print(a)
    else:
        print(b)

elif choice == 4:
    password = input("Enter password: ")
    if password == "Gaurav":
        print("Login Successful")
    else:
        print("Incorrect Password")

else:
    print("Invalid choice")
