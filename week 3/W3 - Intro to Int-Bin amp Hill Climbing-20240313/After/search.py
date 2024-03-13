from random import choice


def hill_climb(search_space):
    """Hill climbs a given search space.

    Args:
        search_space (Population): A Population of solutions

    Returns:
        Individual: Local optimum Individual found in the search.
    """
    # init curr sol at random
    start = choice(search_space)
    print(f"Initial position {start}")
    position = start
    # repeat
    while True:
        # find the best neighbour
        n_list = position.get_neighbours()
        n_fit = [ne.fitness for ne in n_list]
        best_n = n_list[n_fit.index(max(n_fit))]
        # compare
        if best_n.fitness >= position.fitness:
            print(f"Better solution found: {best_n}")
            #replace the current solution
            position = best_n
        else:
            # no better neighbours
            print(f"Best solution found: {position}")
            return position


