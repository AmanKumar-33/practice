class Student:
    def__init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw,"Slytherin"]:
                raise valueError("Invalid House")
        

        self.name = name
        self.house = house
    
def main():
     
    student = get_student()
    print("f{'student.name'} from {'student.house'}")
 
def get_student():
    name = input("name: ")
    house = input("house: ")
    try:
           return Student(name,house)
           

    
     


if __name__ == "__main__":
    main()
