def meow(n: int) -> str:
    # for _ in range(n):
    #     print("meow")
    """ 
    meow n times.
    :param n :number of times of meow
    :type n :int
    :raise typeError if n is not an int
    :return : A string ofn meows , one per line
    :rtype :str
    
    
    """
    return "meow\n" * n


number :int = int(input("enter the number:"))
# meow(number)
meows: str = meow(number)
print(meows)