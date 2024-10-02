def email_slicer():
    while True:
        email = input("Enter the email: ").strip()
        if "@" not in email:
            print ("Please enter a valid email address.")
        elif email.count("@") != 1:
            print ("Invalid email. Email should contain exactly one '@' symbol.")
        else:
            index = email.index("@")
            username = email[:index]
            domain = email[index+1:]
            return f"Your username is {username} and the domain is {domain}."


print(email_slicer())

