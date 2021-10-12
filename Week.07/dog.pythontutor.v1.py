# from dog import *
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

a = Dog()
print(a)
a.wag_tail()

b = Dog(age=2, colour="black", size="Great Dane big")
print(b)

a.bark()
b.bark()
a.bark("even more loudly")
b.bark("loud plus infinity")

# http://pythontutor.com/visualize.html#code=class%20Dog%3A%0A%20%20%20%20def%20__init__%28self,%20age%3D0,%20colour%3D%22brown%22,%20size%3D%22medium%22%29%3A%0A%20%20%20%20%20%20%20%20self.age%20%3D%20age%0A%20%20%20%20%20%20%20%20self.colour%20%3D%20colour%0A%20%20%20%20%20%20%20%20self.size%20%3D%20size%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20s%20%3D%20%22I%20am%20a%20%22%20%2B%20self.colour%20%2B%20%22%20dog,%20of%20age%20%22%0A%20%20%20%20%20%20%20%20s%20%2B%3D%20str%28self.age%29%20%2B%20%20%22,%20of%20size%20%22%20%2B%20self.size%0A%20%20%20%20%20%20%20%20return%28s%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20s%20%3D%20%22Id%3C%22%2B%20str%28id%28self%29%29%20%2B%20%22%3E%20%22%20%2B%20self.colour%20%2B%20%22%20dog%22%0A%20%20%20%20%20%20%20%20return%28s%29%0A%0A%20%20%20%20def%20wag_tail%28self,%20speed%3D%22slowly%22%29%3A%0A%20%20%20%20%20%20%20%20print%28%22See%20my%22,%20self.colour,%20%22tail%20wagging%22,%20speed%29%0A%0A%20%20%20%20def%20bark%28self,%20speed%3D%22loudly%22%29%3A%0A%20%20%20%20%20%20%20%20print%28%22I%20am%20barking%22,%20speed,%20%22said%20the%22,%20self.colour,%20%22dog!%22%29%0A%20%20%0Aa%20%3D%20Dog%28%29%0Aprint%28a%29%0Aa.wag_tail%28%29%0A%0Ab%20%3D%20Dog%28age%3D2,%20colour%3D%22black%22,%20size%3D%22Great%20Dane%20big%22%29%0Aprint%28b%29%0A%0Aa.bark%28%29%0Ab.bark%28%29%0Aa.bark%28%22even%20more%20loudly%22%29%0Ab.bark%28%22loud%20plus%20infinity%22%29&cumulative=true&heapPrimitives=true&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
