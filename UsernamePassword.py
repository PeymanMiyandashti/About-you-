correct_username = "peyman"
correct_password = "Grace2"

for attempt in range(1, 4):
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Access granted!")
        break
    else:
        print(f"Invalid Username or password ! Try again . Attempt {attempt} of 3.")

        if attempt == 3:
            print("Access denied. Too many failed !!! You used all attempts! plz try after 1 hour .")