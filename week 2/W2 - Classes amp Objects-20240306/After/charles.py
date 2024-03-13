from data import cities, distance_matrix
from random import shuffle


class Individual:
    # initializing the attributes of Individual
    # self is a standard notation that refers to the object
    def __init__(self, representation):
        self.representation = representation
        self.distance = distance(self.representation)

    # the rest defines how you want the class to be returned
    # (overwrite what is being returned)
    # they are called dunder or magic methods

    # representation of the object (what we see when we print it)
    def __repr__(self):
        return f"My tour: {self.representation}, distance: {self.distance}"

    # the rest helps us to use len and indexes just like in lists
    # without these, we will get an error for index operations and len function
    # list is also a class predefined by Python
    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value
        self.distance = distance(self.representation)


# function to calculate the distance of a circular path
def distance(path):
    total = 0
    for i in range(len(path)):
        # starting from the distance bw the last city and the first
        total += distance_matrix[path[i - 1]][path[i]]
    return total


# turning the names of the cities into numbers. for ex. NY -> 0
my_path = [i for i in range(len(cities))]
shuffle(my_path)
my_path = Individual(my_path)
print(my_path)

