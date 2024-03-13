from random import choice


def hill_climb(search_space):
    """Hill climbs a given search space.


    Args:
        search_space (Population): A Population of solutions

    Returns:
        Individual: Local optima Individual found in the search.
    """
    #initial solution at random
    start = choice(search_space)
    #current position
    position = start
    print(f"Initial position: {start}")
    while True:
        #get neighbours
        n = position.get_neighbours()
        #get their fitness
        n_fit = [i.fitness for i in n]
        best_n = n[n_fit.index(max(n_fit))]

        if best_n.fitness  >= position.fitness:
            print(f"Found better solution: {best_n}")
            #replece the current soluton
            position = best_n
        # all my neighbours are worse than me
        else:
            print(f"Best solution found: {position}")
            return position



