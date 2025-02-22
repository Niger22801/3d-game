import pygame
from settings import *
from player import Player
from sprite_objects import *
from ray_casting import ray_casting
from drawing import Drawing
from sprite_objects import yy
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))

sprites = Sprites()
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    drawing.background(player.angle)
    walls = ray_casting(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick()