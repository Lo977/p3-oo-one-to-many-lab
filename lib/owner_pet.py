class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all =[]
    def __init__(self,name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception("Not a valid pet type.")    
        self._pet_type = pet_type

class Owner:

    def __init__(self,name):
        self.name = name
        
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
   
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise Exception(" Input object is not of type Pet")
        pet.owner = self
        pass
    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet:pet.name)
        pass

        
# pet1 = Pet("Fido","dog")

# pet2 = Pet("Whisker","cat") 
# pet3 = Pet("Tweety","bird")

# owner1 = Owner("Mike")

# owner1.add_pet(pet1)
# owner1.add_pet(pet2)
# owner1.add_pet(pet3)

# sorted_pets = owner1.get_sorted_pets()
# for pet in sorted_pets:
#     print(f"'{pet.name}' is pet type of:'{pet.pet_type}'")
# print(owner1.pets(owner1))
   
