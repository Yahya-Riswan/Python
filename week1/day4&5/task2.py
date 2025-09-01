class Animal:
    def __init__(self, name, price, locked):
        self.name = name
        self.price = price
        self.locked = locked
    
    def lock(self):
        self.locked = True
        
    def unlock(self):
        self.locked = False



class Dog(Animal):
    def __init__(self, name, price, locked, breed):
        super().__init__(name, price, locked)
        self.breed = breed
    
    def speak(self):
        return "Woof! Woof!"
    
    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed}, price={self.price}, locked={self.locked})"



d1 = Dog("Tommy", 5000, False, "Labrador")

print(d1)             
print(d1.speak())      
d1.lock()
print("Locked:", d1.locked) 
d1.unlock()
print("Locked:", d1.locked) 