from search import hill_climb
from charles import Population, Individual


def get_fitness(self):
    """A fitness function that takes a base-10 number,
    transforms it into base-2 (binary), and returns the
    number of 1's occuring in the binary representation.

    Returns:
        int: the number of 1's in the binary representation.
    """
    return "{0:04b}".format(self.representation[0]).count("1")



def get_neighbours(self):
    """A neighbourhood function for int_bin problem
    Returns:
        Individual: +1 and -1 of the number
    """
    if self.representation[0] == 1:
        return (Individual(representation=[self.representation[0] + 1]),)

    if self.representation[0] == 15:
        return (Individual(representation=[self.representation[0] - 1]),)

    n1 = Individual(representation=[self.representation[0] + 1])
    n2 = Individual(representation=[self.representation[0] - 1])
    return n1, n2


# Monkey patching: overwriting the functions
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours


# search space
pop = Population(size=1,
                 optim="max",
                 sol_size=1,
                 valid_set=[i for i in range(1,16)])

hill_climb(pop)



