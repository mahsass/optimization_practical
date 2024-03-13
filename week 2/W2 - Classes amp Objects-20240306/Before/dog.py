class Dog:
    def __init__(self,name,breed,age):
        self.Name = name
        self.Breed = breed
        self.Age = age

    def __repr__(self):
        return f"Name: {self.Name}, Breed: {self.Breed}, Age: {self.Age}"

jack = Dog("Jack", "Husky", 5)
print(jack)
