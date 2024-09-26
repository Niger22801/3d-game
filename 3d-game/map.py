from settings import *
with open("mm.txt", "r") as file:
    str1 = file.readlines()
text_map = str1
world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2':
                world_map[(i * TILE, j * TILE)] = '2'
            elif char == '3':
                world_map[(i * TILE, j * TILE)] = '3'