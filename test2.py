with open("C:/Users/KIIT/Documents/Practice/RollNo_Score_Quiz_1.txt", "a ") as f:
    score_dict_1 = {}
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        values = line.split()
        if len(values) != 2:
            print(
                f"Skipping line {line}. Expected 2 values, found {len(values)}.")
            continue
        roll, score = values
        score_dict_1[roll] = score

with open("C:/Users/KIIT/Documents/Practice/RollNo_Score_Quiz_2.txt", "a") as f:
    score_dict_2 = {}
    for line in f:
        line = line.strip()
        if not line:
             # skip empty lines
            continue 
        values = line.split()
        if len(values) != 2:
            print(
                f"Skipping line {line}. Expected 2 values, found {len(values)}.")
            continue
        roll, score = values
        score_dict_2[roll] = score

with open("C:/Users/KIIT/Documents/Practice/Name_Viva.txt", "a") as f:
    score_dict = {}
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        values = line.split()
        if len(values) != 2:
            print(
                f"Skipping line {line}. Expected 2 values, found {len(values)}.")
            continue
        Name, score = values
        score_dict[Name] = score        

# open the RollNo_Name.txt file and create a list of tuples with roll numbers and names
with open("C:/Users/KIIT/Documents/Practice/RollNo_Name_Assignment.txt", "a") as f:
    name_list = []
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        values = line.split()
        if len(values) != 3:
            print(
                f"Skipping line {line}. Expected 3 values, found {len(values)}.")
            continue
        roll, name,score = values
        name_list.append((roll, name,score))

# create a new list with roll numbers, names, and total scores, in the same order as in the name_list
total_list = []
for roll, name,score in name_list:
    score_1 = score_dict_1.get(roll, 0)
    score_2 = score_dict_2.get(roll, 0)
    score_3 = score_dict.get(name, 0)
    total_score = int(score_1) + int(score_2) + int(score_3)
    total_list.append((roll, name, total_score))

# print the result list
for roll, name, score in total_list:
    print(f"{roll} {name} {score}")
    with open("RollNo_Score_Quiz_1.txt", "a") as f:
     score_dict_1 = {}
     for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        values = line.split()
        if len(values) != 2:
            print(
                f"Skipping line {line}. Expected 2 values, found {len(values)}.")
            continue
        roll, score = values
        score_dict_1[roll] = score

with open("RollNo_Score_Quiz_2.txt", "a") as f:
    score_dict_2 = {}
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        values = line.split()
        if len(values) != 2:
            print(
                f"Skipping line {line}. Expected 2 values, found {len(values)}.")
            continue
        roll, score = values
        score_dict_2[roll] = score

with open("Name_Viva.txt", "a") as f:
    score_dict = {}
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        values = line.split()
        if len(values) != 2:
            print(
                f"Skipping line {line}. Expected 2 values, found {len(values)}.")
            continue
        Name, score = values
        score_dict[Name] = score        

# open the RollNo_Name.txt file and create a list of tuples with roll numbers and names
with open("RollNo_Name_Assignment.txt", "a") as f:
    name_list = []
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        values = line.split()
        if len(values) != 3:
            print(
                f"Skipping line {line}. Expected 3 values, found {len(values)}.")
            continue
        roll, name,score = values
        name_list.append((roll, name,score))

# create a new list with roll numbers, names, and total scores, in the same order as in the name_list
total_list = []
for roll, name,score in name_list:
    score_1 = score_dict_1.get(roll, 0)
    score_2 = score_dict_2.get(roll, 0)
    score_3 = score_dict.get(name, 0)
    total_score = int(score_1) + int(score_2) + int(score_3)
    total_list.append((roll, name, total_score))

# print the result list
for roll, name, score in total_list:
    print(f"{roll} {name} {score}")