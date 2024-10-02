def email_slicer():
    email = input("Enter the email: ").strip()
    if "@" not in email:
        return "Please enter a valid email address."
    elif email.count("@") != 1:
        return "Invalid email. Email should contain exactly one '@' symbol."
    else:
        index = email.index("@")
        username = email[:index]
        domain = email[index+1:]
        return f"Your username is {username} and the domain is {domain}."


print(email_slicer())

