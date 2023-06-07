email = int (input("enter Your email:"))


username,domain = email.split("@")
if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")