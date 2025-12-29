#221002268 - Sheikh Adnan Mostofa

import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, target, R, C):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_cost = {start: 0}

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_cost[target]

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)

            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                new_g = g_cost[current] + 1

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f = new_g + manhattan(neighbor, target)
                    heapq.heappush(open_set, (f, neighbor))
                    came_from[neighbor] = current

    return None, None

with open("input.txt", "r") as file:
    R, C = map(int, file.readline().split())
    grid = [list(map(int, file.readline().split())) for _ in range(R)]
    sr, sc = map(int, file.readline().split())
    tr, tc = map(int, file.readline().split())

start = (sr, sc)
target = (tr, tc)

path, cost = astar(grid, start, target, R, C)


if path:
    print(f"Path found with cost {cost} using A*")
    print(f"Shortest Path: {path}")
else:
    print("Path not found using A*")
