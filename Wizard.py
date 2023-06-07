# Inheritance
# 
class wizard:
    def __init__(self,name,house):
        if not name:
            raise ValueError("missing name")
        self.name = name


            

class student(wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house
      


class Professor(wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
        

wizard = wizard("Albus")
student = student("harry","Gryffindor")
Professor  = Professor("severus","Defence against the dark Arts")