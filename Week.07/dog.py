class Dog:
    def __init__(self, age=0, colour="brown", size="medium"):
        self.age = age
        self.colour = colour
        self.size = size

    def __str__(self):
        s = "I am a " + self.colour + " dog, of age "
        s += str(self.age) +  ", of size " + self.size
        return(s)

    def __repr__(self):
        s = "Id<"+ str(id(self)) + "> " + self.colour + " dog"
        return(s)

    def wag_tail(self, speed="slowly"):
        print("See my", self.colour, "tail wagging", speed)

    def bark(self, speed="loudly"):
        print("I am barking", speed, "said the", self.colour, "dog!")
