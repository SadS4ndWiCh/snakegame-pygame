from pygame import Vector2

import random

from constants import TILE_SIZE, WIDTH,  HEIGHT, SPAWN_PADDING

def random_grid_pos(use_padding: bool = False) -> Vector2:
  if(not use_padding):
    x_rand = random.randint(0, WIDTH / TILE_SIZE)
    y_rand = random.randint(0, HEIGHT / TILE_SIZE)

    return Vector2(x_rand * TILE_SIZE, y_rand * TILE_SIZE)
  else:
    tile_padding = TILE_SIZE * SPAWN_PADDING

    x_rand = random.randint(
      SPAWN_PADDING,
      (WIDTH - tile_padding) / TILE_SIZE
    )
    y_rand = random.randint(
      SPAWN_PADDING,
      (HEIGHT - tile_padding) / TILE_SIZE
    )

    return Vector2(x_rand * TILE_SIZE, y_rand * TILE_SIZE)