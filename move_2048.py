import copy

def move_row_left(row):
    new_row=copy.copy(row)
    for y in range(1,len(new_row)):
        if new_row[y] not in [0," "]:
            while y>0 and new_row[y-1] in [0," "]:
                new_row[y-1], new_row[y] = new_row[y], " "
                y-=1
            if y>0 and new_row[y-1]==new_row[y]:
                new_row[y-1], new_row[y] = 2*new_row[y-1], " "
    return new_row

def move_row_right(row):
    new_row=copy.copy(row)
    new_row.reverse()
    new_row=move_row_left(new_row)
    new_row.reverse()
    return new_row

def move_grid(grid,d):
    new_grid=copy.deepcopy(grid)
    if d=="g":
        for x in range(len(new_grid)):
            new_grid[x]=move_row_left(new_grid[x])
    elif d=="d":
        for x in range(len(new_grid)):
            new_grid[x]=move_row_right(new_grid[x])
    elif d=="h":
        for y in range(len(new_grid[0])):
            column=[x[y] for x in grid]
            column=move_row_left(column)
            for x in range(len(column)):
                new_grid[x][y]=column[x]
    elif d=="b":
        for y in range(len(new_grid[0])):
            column=[x[y] for x in grid]
            column=move_row_right(column)
            for x in range(len(column)):
                new_grid[x][y]=column[x]
    return new_grid
