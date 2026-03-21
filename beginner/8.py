class Avengers:
    def __init__(self, name, age, gender, superpower, weapon ):
        self.name = name
        self.age = age
        self.gender = gender
        self.superpower = superpower
        self.weapon = weapon
        super_heroes=["Captain America", "Iron Man", "Black Widow", "Hulk",
"Thor", "Hawkeye"] 
        method_is_leader = self.name == "Captain America"
        if method_is_leader:
            print(f"{self.name} is the leader of the Avengers.")
        
    def display(self):
        print(f"{self.name} has the power of {self.superpower}.")
        
class CaptainAmerica(Avengers):
    def __init__(self, name, age, gender, superpower, weapon):
        name="Captain America"
        age=100
        gender="Male"
        superpower="Super strength"
        weapon="Vibranium shield"
        method_is_leader = name == "Captain America"
        super().__init__(name, age, gender, superpower, weapon)
class IronMan(Avengers):
    def __init__(self, name, age, gender, superpower, weapon):
        name="Iron Man"
        age=48          
        gender="Male"
        superpower="Genius-level intellect"
        weapon="Powered armor suit"
        super().__init__(name, age, gender, superpower, weapon) 
class BlackWidow(Avengers):
    def __init__(self, name, age, gender, superpower, weapon):
        name="Black Widow"
        age=35
        gender="Female"
        superpower="Master martial artist"
        weapon="Widow's Bite"
        super().__init__(name, age, gender      , superpower, weapon) 
class Hulk(Avengers):
    def __init__(self, name, age, gender, superpower, weapon):
        name="Hulk"
        age=49              
        gender="Male"       
        superpower="Superhuman strength"
        weapon="None"
        super().__init__(name, age, gender, superpower, weapon) 
class Hawkeye(Avengers):
    def __init__(self, name, age, gender, superpower, weapon):
        name="Hawkeye"
        age=40
        gender="Male"
        superpower="Master archer"
        weapon="Bow and arrows"
        super().__init__(name, age, gender, superpower, weapon)
class Thor(Avengers):
        def __init__(self, name, age, gender, superpower, weapon):
            name="Thor"
            age=1500
            gender="Male"
            superpower="Super energy"
            weapon="Mjolnir"
            super().__init__(name, age, gender, superpower, weapon) 

   