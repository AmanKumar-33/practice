class Cat:
    MEWOS = 3


    def meows(self):
        for _ in range(Cat.MEWOS):
            print("meow")

    
cat = Cat()
cat.meows()