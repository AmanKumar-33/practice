email = input("what's your email:").rstrip()


if "@"in email and "." in email:
    print("valid")
else:
    print("not valid")