def readline_returnList(filename):
	name_list=[]
	file=open(filename)
	for _ in file.readlines():
		name_list.append(_.rstrip("\n"))
	return(name_list)

filename1='C:/Users/KIIT/Documents/Practice/student1.csv'
filename2='C:/Users/KIIT/Documents/Practice/student1.csv'
studentlist1=readline_returnList(filename1)
studentlist2=readline_returnList(filename2)

# Merge the two student lis   t.
print(studentlist1)
print(studentlist2)
l=studentlist1
l.extend(studentlist2)
for i in l:
   print(l)


# Count how many times 'PRIYANSHU' and 'HIMANSHU' present in the first student list.
print("no of priyanshu:",l.count("PRIYANSHU"),"no of HIMANSHU:",l.count("HIMANSHU"))


# Sort all the name of the student in two student list. 
studentlist1.sort()
studentlist2.sort()
l.sort()
print(l)

# Remove the duplicate valuse present in student list.
a=[]
[a.append(x)for x in l if x not in a]
print(a)

# find the no of student with starting capital A
check ='A'
res = []
for i in l:
    if(i.find(check) == 0 or i.find(check.lower()) == 0):
        res.append(i)
print("The list of matching first letter : " + str(res))

