from data import cities, distance_matrix
from random import shuffle

class Individual:
    def __init__(self,representation):
        self.representation = representation
        self.distance = distance(self.representation)
    def __repr__(self):
        return f"My path: {self.representation}, distance: {self.distance}"

    def __len__(self):
        return le(sel.representation)
    def __getitem__(self, position):
        return self.representation[position]
    def __setitem__(self, position, value):
        self.representation[poition]= value

jack = Dog("jack","Husky",5)
print(jack.Name)
# function to calculate the distance of a circular path
def distance(path):
    total = 0
    for i in range(len(path)):
        # starting from the distance bw the last city and the first
        total += distance_matrix[path[i-1]][path[i]]
    return total


# turning the names of the cities into numbers. for ex. NY -> 0
my_path = [i for i in range(len(cities))]
#shuffle(my_path)
print(f"My tour: {my_path}, distance: {distance(my_path)}")
