class House():
    def __init__(self, type, location, owner):
        self.type = type
        self.location = location
        self.owner = owner

owner_one = House("Bungalow", "Kitengela", "Vannessa")
print(owner_one.type)
print(owner_one.location)
print(owner_one.owner)

owner_two = House("Pent house", "Kajiado", "Mutavi")
print(owner_two.type)
print(owner_two.location)
print(owner_two.owner)




