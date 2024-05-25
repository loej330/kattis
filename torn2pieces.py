data = [
    "FirstStop SecondStop\n"
    "SecondStop FirstStop ThirdStop\n",
    "FifthStop FourthStop SixthStop\n",
    "SixthStop FifthStop\n",
    "FirstStop FifthStop\n"
]

def do():
    grid = {} 
    # for _ in range(int(input())):
    for _ in range(4):
    #     station, *neighbors = input().split()
        station, *neighbors = data[_].split()

        if station not in grid: grid[station] = set()
        for neighbor in neighbors:
            if neighbor not in grid: 
                grid[neighbor] = set()
            if neighbor not in grid[station]:
                grid[station].add(neighbor)
            if station not in grid[neighbor]:
                grid[neighbor].add(station)

    start, dest = data[-1].split()
    # start, dest = input().split()
    paths = [[start]]
    print("GRID: ", grid)
    while True:
        print(paths)
        input("press any key to continue looping")
        next_paths = []
        for path in paths:
            current = path[-1]
            for neighbor in grid[current]:
                if current == dest: return(path)
                elif neighbor not in path: next_paths += [ path + [neighbor] ]
        paths = next_paths

do()
# print(" ".join(do()))
