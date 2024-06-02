#!/usr/bin/env python3

class Dog:
    pass
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

    
beast = Dog("Beast", "Alsatian")

beast.name
print(beast.name)

beast.breed
print(beast.breed)


