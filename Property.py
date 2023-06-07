# @prperty
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    def house(self):
        return self.house
    # setter
    def house(self,house):
        self.house = house

    
def main():
    student = get_Student()
    student.house = "Number four,private Drive"
    print(student)
    