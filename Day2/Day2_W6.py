# W6. Simulate a login system with 3 attempts

correct_username = "sunny"
correct_password = "1234"

attempts = 1

while attempts <= 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong details")
        attempts += 1
