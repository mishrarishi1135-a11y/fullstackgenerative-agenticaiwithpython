# property decorator --> Getter and Setter
class TeaLeaf:
    def __init__(self,age):
        self._age = age


    @property
    def age(self):
            return self._age + 2

    @age.setter   # this is how you set the value inside the class.
    def age(self,age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea Leaf age must between 1 and 5 years")

Leaf = TeaLeaf(2)
print(Leaf.age)
Leaf.age = 4
print(Leaf.age)

# but if we provide the value of Leaf.age = 6 then it show error.