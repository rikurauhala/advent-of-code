grid = [line.strip() for line in open("input.txt")]

directions = {
    "N": "|7F",
    "S": "|JL",
    "W": "-FL",
    "E": "-7J",
}

def get_starting_char(row, col):
    neighbors = {
        "N": grid[row-1][col],
        "S": grid[row+1][col],
        "W": grid[row][col-1],
        "E": grid[row][col+1],
    }

    for _, symbols in directions.items():
        if all(neighbors[direction] in symbols for direction in neighbors):
            return symbols[0]

for row_index, row in enumerate(grid):
    for col_index, char in enumerate(row):
        if char == "S":
            start_row = row_index
            start_col = col_index
            starting_char = get_starting_char(row_index, col_index)
            grid[row_index] = grid[row_index].replace("S", starting_char)
            break

current = (start_row-1, start_col) # TODO: base on starting char
visited = [(start_row, start_col)]
length = 1

while current not in visited:
    visited.append(current)
    row, col = current[0], current[1]
    tile = grid[row][col]
    
    north = grid[row - 1][col] if row - 1 >= 0 else None
    can_move_north = north in directions["N"] and (row - 1, col) not in visited if north is not None else False
    
    south = grid[row + 1][col] if row + 1 < len(grid) else None
    can_move_south = south in directions["S"] and (row + 1, col) not in visited if south is not None else False
    
    west = grid[row][col - 1] if col - 1 >= 0 else None
    can_move_west = west in directions["W"] and (row, col - 1) not in visited if west is not None else False
    
    east = grid[row][col + 1] if col + 1 < len(grid[row]) else None
    can_move_east = east in directions["E"] and (row, col + 1) not in visited if east is not None else False
    
    match tile:
        case "|":
            if can_move_north:
                current = (row-1, col)
            if can_move_south:
                current = (row+1, col)
        case "-":
            if can_move_west:
                current = (row, col-1)
            if can_move_east:
                current = (row, col+1)
        case "L":
            if can_move_north:
                current = (row-1, col)
            if can_move_east:
                current = (row, col+1)
        case "J":
            if can_move_north:
                current = (row-1, col)
            if can_move_west:
                current = (row, col-1)
        case "7":
            if can_move_south:
                current = (row+1, col)
            if can_move_west:
                current = (row, col-1)
        case "F":
            if can_move_south:
                current = (row+1, col)
            if can_move_east:
                current = (row, col+1)
    length += 1

print(length // 2)
