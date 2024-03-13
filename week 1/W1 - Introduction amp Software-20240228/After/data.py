# one dim. list to keep the city names
cities = ["New York", "Los Angeles", "Chicago", "Minneapolis"]
# two dim. list to keep the distance matrix
distance_matrix = [
    [0, 2451, 713, 1018],
    [2451, 0, 1745, 1524],
    [713, 1745, 0, 355],
    [1018, 1524, 355, 0]]

if __name__ == '__main__':
    print(distance_matrix[0][1])
    print(distance_matrix[1][2])
    print(distance_matrix[2][3])
    print(distance_matrix[-1][0])

    lst = [2 for i in range(4)]
    lst = [element+10 for element in lst]
    print(lst)

    path = [i for i in range(len(cities))]
    print(path)




