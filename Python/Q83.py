# Define a class Person & its two child classes: Male & Female. All classes have a method "getGender" which can print "Male"
# for Male class & "Female" for Female class

class Person:
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"
    
class Female(Person):
    def getGender(self):
        return "Female"
    
person = Person()
male = Male()
female = Female()

print(person.getGender())
print(male.getGender())
print(female.getGender())