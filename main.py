import grid_2048
import textual_2048
import move_2048

size=textual_2048.read_size_grid()
theme=grid_2048.THEMES[textual_2048.read_theme_grid()]
grid= grid_2048.init_game(4)
print(grid_2048.grid_to_string_with_size_and_theme(grid,theme,size))
grid=move_2048.move_grid(grid,"b")
print(grid_2048.grid_to_string_with_size_and_theme(grid,theme,size))
