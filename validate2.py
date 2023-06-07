import re
password = input("enter your Password:-").rstrip()


if re.search(r".+@.+\.edu",password):
    print("valid")
else:
    print("invalid")


