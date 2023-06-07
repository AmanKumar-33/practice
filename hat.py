import random

class Hat:

    houses = ["Gryffindor","Hufflepuff","ravenclaw","slytherin"]
    # @classmethod
    def sort(cls, name):
        # house = random.choice(self.house)
        print(name,"is in",random.choice(cls.houses))

Hat.sort("harry")
# staticmethod
# inheritance
# 