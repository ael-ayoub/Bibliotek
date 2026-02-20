class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        print("B")

class C(A):
    def greet(self):
        print("C")

class D(C,B):
    pass

d = D()
d.greet()
