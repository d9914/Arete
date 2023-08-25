""" 
N Nearest Stores Problem
Implement the functions below.

For n_nearest_without_obstacles, your function should return the N nearest stores to 
the provided input position.

For n_nearest_with_obstacles, your function should return the N nearest stores to the 
provided input position that avoid the obstacles defined in the map file.
"""

# TODO: Add any imports you need for your solution here


from collections import deque
import csv
import math


# Problem 1
"""
    Returns the list of n_stores stores closest to the provided input position (pos)
    using the input file (input_file).

    Parameters
    ----------
    input_file : str
        The path to the .csv input file
    n_stores : int
        The number of stores to return
    pos : tuple
        The position to calculate distance to

    Returns
    -------
    stores : list
        Store names, sorted by closest first
    """
 # TODO: Add your solution to Problem 1 here


def calculate_distance(start_pos,store_pos):
    x1, y1 = start_pos
    x2, y2 = store_pos
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)   # Distance Formula


def n_nearest_without_obstacles(input_file: str, n_stores: int, pos: tuple) -> list:
    try:
        # Get every store and it's distance from pos
        stores=[]
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                store_pos = (int(row[0]), int(row[1]))
                store_name=row[2]
                distance = calculate_distance(pos, store_pos)
                stores.append((store_name, distance))


        # Sort based on distance 
        stores.sort(key=lambda x: x[1])
        nearest_stores=[]
        for i in range(n_stores):
            if i<len(stores):
                nearest_stores.append(stores[i][0])
        return nearest_stores
    
    except FileNotFoundError:
        print("File not found!")
        return []





"""
    Returns the list of n_stores stores closest to the provided input position (pos)
    from the input file (input_file), avoiding obstacles in the map (map_file).

    Parameters
    ----------
    input_file : str
        The path to the .csv input file
    map_file : str
        The path to the .txt map file that defines the grid of traversable cells
    n_stores : int
        The number of stores to return
    pos : tuple
        The position to calculate distance to

    Returns
    -------
    stores : list
        Store names, sorted by closest first
    """
    # TODO: Add your solution to Problem 2 here



def bfs(grid, start_pos, n_stores):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    closest_stores = []
    queue = deque([(start_pos)])
    
     
    while queue and len(closest_stores) < n_stores:
        current_pos = queue.popleft()
        x, y = current_pos

        if grid[x][y] != "." and grid[x][y] != "X":
            store_name = grid[x][y]
            closest_stores.append(store_name)
        
        neighbors=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for next_x, next_y in neighbors:
            if 0 <= next_x < rows and 0 <= next_y < cols and (next_x, next_y) not in visited and grid[next_x][next_y] != "X":
                new_pos = (next_x, next_y)
                queue.append(new_pos)
                visited.add(new_pos)
    return closest_stores

# Problem 2
def n_nearest_with_obstacles(input_file: str, map_file: str, n_stores: int, pos: tuple) -> list:
    try:
    # Building a graph to traverse 
        grid = []
        with open(map_file, 'r') as map_file:
            for line in map_file:
                row = list(line.strip())  
                grid.append(row)


        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                store_x = int(row[0])
                store_y=int(row[1])
                store_name=row[2]
                grid[store_x][store_y]=store_name
        

        # BFS to find closest stores 
        closest_stores = bfs(grid, pos, n_stores)
        
        return closest_stores
        
    except FileNotFoundError:
        print("File not found!")
        return []
    




# Assumed start position will be valid 
if __name__ == "__main__":
    #input_data = "../inp_files/stores.csv"
    input_data = "inp_files\stores.csv"
    #map_data = "../inp_files/stores_map.txt"
    map_data = "inp_files\stores_map.txt"
    n_stores = 4
    start_pos = (0, 0)

    try:
        print(n_nearest_without_obstacles(input_data, n_stores, start_pos))
        print(n_nearest_with_obstacles(input_data, map_data, n_stores, start_pos))
    except Exception as err:
        print(err)
