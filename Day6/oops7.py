# Here we learn about 3 ways to access base class
class Chai:
    def __init__(self,type_, strength):
        self.type = type_
        self.strength = strength   # This is our basic class.

class GingerChai(Chai):
    def __init__(self,type_,strength,spice_level):
        self.type =type_
        self.strength = strength
        self.spice_level = spice_level
        # this is just little bit of code duplication.

        # Try another way
class GingerChai(Chai):
    def __init__(self,type_,strength,spice_level):
        Chai.__init__(self,type_,strength)
        self.spice_level = spice_level     # we do this by explicit call.

class GingerChai(Chai):
    def __init__(self,type_,strength,spice_level):
        super().__init__(type_,strength)
        self.spice_level = spice_level        # by using the super() method.