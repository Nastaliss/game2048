import grid_2048
import textual_2048
import move_2048
import random

def random_play():
    dic_move={0:"g",1:"d",2:"h",3:"b"}
    grid=grid_2048.init_game(4)
    print("Situation de départ :")
    print(grid_2048.grid_to_string_with_size_and_theme(grid,grid_2048.THEMES["0"],4))
    tour=1
    while not move_2048.is_game_over(grid) and grid_2048.get_grid_tile_max(grid)<2048:
        moves=move_2048.move_possible(grid)
        index=[i for i in range(4) if moves[i]]
        choice=random.choice(index)
        grid=move_2048.move_grid(grid,dic_move[choice])
        if not grid_2048.is_full_grid(grid):
            grid=grid_2048.grid_add_new_tile(grid)
        print("Tour {}, deplacement {} :".format(tour, dic_move[choice]))
        print(grid_2048.grid_to_string_with_size_and_theme(grid,grid_2048.THEMES["0"],4))
        tour+=1
    if grid_2048.get_grid_tile_max(grid)>=2048 :
        return "Victoire !"
    return "Game Over"

def game_play():
    dic_move={0:"g",1:"d",2:"h",3:"b"}
    size=int(textual_2048.read_size_grid())
    theme=grid_2048.THEMES[textual_2048.read_theme_grid()]
    grid=grid_2048.init_game(size)
    print("Situation de départ :")
    print(grid_2048.grid_to_string_with_size_and_theme(grid,theme,size))
    tour=1
    while not move_2048.is_game_over(grid) and grid_2048.get_grid_tile_max(grid)<2048:
        moves=move_2048.move_possible(grid)
        commands_possible=[dic_move[i] for i in range(4) if moves[i]]
        command=textual_2048.read_player_command()
        while not command in commands_possible :
            print("Deplacement impossible")
            command=textual_2048.read_player_command()
        grid=move_2048.move_grid(grid,command)
        if not grid_2048.is_full_grid(grid):
            grid=grid_2048.grid_add_new_tile(grid)
        print("Tour {}, deplacement {} :".format(tour, command))
        print(grid_2048.grid_to_string_with_size_and_theme(grid,theme,size))
        tour+=1
    if grid_2048.get_grid_tile_max(grid)>=2048 :
        return "Victoire !"
    return "Game Over"

if __name__ == '__main__':
    game_play()
    exit(1)

