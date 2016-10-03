def map_gen(size):
    """Returns a list of tupled coordinates in grid of SIZE
    size = int"""
    map = []
    for x in range(size):
        for y in range(size):
            map.append((x, y))
    return map
