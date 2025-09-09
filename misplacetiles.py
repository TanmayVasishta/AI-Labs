goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]

def misplaced_tiles_heuristic(current_state, goal_state):
    misplaced_count = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            if current_state[i][j] != 0 and current_state[i][j] != goal_state[i][j]:
                misplaced_count += 1
    return misplaced_count

def get_blank_position(state):
    for r in range(len(state)):
        for c in range(len(state[r])):
            if state[r][c] == 0:
                return r, c
    return None

def apply_move(state, dr, dc):
    r, c = get_blank_position(state)
    rows, cols = len(state), len(state[0])
    new_r, new_c = r + dr, c + dc

    if 0 <= new_r < rows and 0 <= new_c < cols:
        new_state = [row[:] for row in state] # Create a copy
        new_state[r][c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[r][c]
        return new_state
    return None

current_state = initial_state
print("Initial State:")
for row in current_state:
    print(row)
print(f"Heuristic value (misplaced tiles): {misplaced_tiles_heuristic(current_state, goal_state)}")
print("-" * 20)

# Example moves: move the blank tile right, then down
move1_state = apply_move(current_state, 0, 1) # Move right
if move1_state:
    print("After moving blank right:")
    for row in move1_state:
        print(row)
    print(f"Heuristic value (misplaced tiles): {misplaced_tiles_heuristic(move1_state, goal_state)}")
    print("-" * 20)
    current_state = move1_state # Update current state for the next move

move2_state = apply_move(current_state, 1, 0) # Move down
if move2_state:
    print("After moving blank down:")
    for row in move2_state:
        print(row)
    print(f"Heuristic value (misplaced tiles): {misplaced_tiles_heuristic(move2_state, goal_state)}")
    print("-" * 20)