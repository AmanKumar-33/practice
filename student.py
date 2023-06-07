
student=[]
with open("C:\Users\KIIT\Documents\Practice\python\student1.csv")as file:
    for line in file:
        student.append(line.rstrip())

for i in sorted(student,reverse=True):
    print(f"hello,{student}")
