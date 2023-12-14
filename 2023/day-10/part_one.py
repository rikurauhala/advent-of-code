grid = [line.strip() for line in open('input.txt')]
start_x, start_y = 0, 0

for row_index, row in enumerate(grid):
    for col_index, char in enumerate(row):
        if char == 'S':
            start_x = row_index
            start_y = col_index
            grid[row_index] = grid[row_index].replace('S', '|')
            break

current = (start_x - 1, start_y)
visited = []
visited.append((start_x, start_y))
length = 1

while current not in visited:
    visited.append(current)
    row, col = current[0], current[1]
    tile = grid[row][col]
    
    north = grid[row - 1][col] if row - 1 >= 0 else None
    can_move_north = north in "|7F" and (row - 1, col) not in visited if north is not None else False
    
    south = grid[row + 1][col] if row + 1 < len(grid) else None
    can_move_south = south in "|JL" and (row + 1, col) not in visited if south is not None else False
    
    west = grid[row][col - 1] if col - 1 >= 0 else None
    can_move_west = west in "-FL" and (row, col - 1) not in visited if west is not None else False
    
    east = grid[row][col + 1] if col + 1 < len(grid[row]) else None
    can_move_east = east in "-7J" and (row, col + 1) not in visited if east is not None else False
    
    match tile:
        case "|":
            if can_move_south:
                current = (row + 1, col)
            elif can_move_north:
                current = (row - 1, col)
        case "-":
            if can_move_west:
                current = (row, col - 1)
            elif can_move_east:
                current = (row, col + 1)
        case "L":
            if can_move_north:
                current = (row - 1, col)
            elif can_move_east:
                current = (row, col + 1)
        case "J":
            if can_move_north:
                current = (row - 1, col)
            elif can_move_west:
                current = (row, col - 1)
        case "7":
            if can_move_south:
                current = (row + 1, col)
            elif can_move_west:
                current = (row, col - 1)
        case "F":
            if can_move_south:
                current = (row + 1, col)
            elif can_move_east:
                current = (row, col + 1)
    length += 1

print(length // 2)
