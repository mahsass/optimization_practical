from random import shuffle, choice, sample

class Individual:
    # initializing the attributes of Individual
    # self is a standard notation that refers to the object
    def __init__(self, representation=None, size=None, valid_set=None):

        if representation == None:
            # individual will be chosen from the valid_set with a specific size
            self.representation = sample(valid_set, size)

        # if we pass an argument like Individual(my_path)
        else:
            self.representation = representation

        # fitness will be assigned to the individual
        self.fitness = self.get_fitness()

    # methods for the class
    def get_fitness(self):
        pass

    def get_neighbours(self):
        pass


    # the rest defines how you want the class to be returned
    # (overwrite what is being returned)
    # they are called dunder or magic methods

    # representation of the object (what we see when we print it)
    def __repr__(self):
        return f"Individual: {self.representation}; Fitness: {self.fitness}"

    # the rest helps us to use len and indexes just like in lists
    # without these, we will get an error for index operations and len function
    # list is also a class predefined by Python
    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value


class Population:
    def __init__(self, size, optim, **kwargs):

        # population size
        self.size = size

        # defining the optimization problem as a minimization or maximization problem
        self.optim = optim

        self.individuals = []

        # appending the population with individuals
        for _ in range(size):
            self.individuals.append(
                Individual(
                    size=kwargs["sol_size"],
                    valid_set=kwargs["valid_set"],
                )
            )

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

