def Password_strength_check():
    Password = input("write your password: ")
    Password_length = len(Password)
    Rating = 0

    if Password_length < 8:
        Rating = 0
    elif 8 <= Password_length <= 11:
        Rating = 1
    elif Password_length >= 12:
        Rating = 2
    
    if any(char.islower() for char in Password):
        Rating += 1
    if any(char.isupper() for char in Password):
        Rating += 1
    if any(char.isdigit() for char in Password):
        Rating += 1
    if any(not char.isalnum() for char in Password):
        Rating += 1
    
    for bad_words in ["123456, admin"]:
        if bad_words in Password:
            Rating -= 2

    if Rating <= 0:
        print("Weak password")
    elif 1 <= Rating <= 3:
        print("Medium password")
    elif Rating >= 4:
        print("Strong password")

Password_strength_check()