class Person:
    def __init__(s, firstname, lastname):
        s.firstname = firstname
        s.lastname = lastname

    def printname(s):
        print (s.firstname , s.lastname)

class child(Person):
    def __init__(s, fname, lname):
        # Person.__init__(fname, lname)
        Person(fname, lname)
        # s.age = age

    def printAge(s):
        print (s.age)

c1 = child("ayoub", "no isssaoui")

# c1.printAge()
print(c1.firstname)
print (c1.age)
p1 = Person("ayoub", "issaoui")
p1.printname()
