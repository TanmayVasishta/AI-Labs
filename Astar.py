import heapq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Manhattan distance heuristic
def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val-1)//3
                goal_y = (val-1)%3
                dist += abs(i-goal_x) + abs(j-goal_y)
    return dist

# Generate neighbors
def neighbors(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            yield new_state

# Convert state to tuple
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* algorithm
def astar(start):
    open_list = [(manhattan(start), 0, start, [])]
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        if state == goal:
            return path + [state]
        visited.add(to_tuple(state))
        for n in neighbors(state):
            if to_tuple(n) not in visited:
                new_g = g + 1
                heapq.heappush(open_list, (new_g + manhattan(n), new_g, n, path + [state]))
    return None

def print_state(state):
    for row in state:
        print(row)
    print()

# Example
if __name__ == "__main__":
    start = [[1,2,3],
             [4,0,6],
             [7,5,8]]

    print("Initial State:")
    print_state(start)
    sol = astar(start)
    if sol:
        print("Moves needed:", len(sol)-1)
        for s in sol:
            print_state(s)
    else:
        print("No solution found.")