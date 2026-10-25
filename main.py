class FamilyMember:
    def __init__(self, eye_colour, height_cm):
        self.eye_colour = eye_colour
        self.height_cm = height_cm
    def show_traits(self):
        print("eye colour", self.eye_colour)
        print("height cm", self.height_cm)
class kid(FamilyMember):
    def __init__(self, eye_colour, height_cm, name, age):
        self.name = name
        self.age = age
        super().__init__( eye_colour, height_cm)
    def show_traits(self):
        print("name: ",self.name)
        print("age: ",self.age)
    def favorite_hobby(self, hobby):
        print(self.name, "loves", hobby)
child = kid("rainbow",100,"abdullah maqsood",8)
child.show_traits()
child.favorite_hobby("playing video games")
print("is kid a subclass of family member?",issubclass(kid,FamilyMember))