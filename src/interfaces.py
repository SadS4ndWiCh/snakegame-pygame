from pygame.locals import *

import colorsys

class Colors:
  BLACK = (0, 0, 0)
  WHITE = (255,255,255)
  RED = (255, 0, 0)
  YELLOW = (255, 255, 0)

  def color_by_hue(hue: float) -> list[int]:
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    
    return int(255 * r), int(255 * g), int(255 * b)

class MoveDirection:
  LEFT = 0
  UP = 1
  DOWN = 2
  RIGHT = 3

class GameStates:
  RUNNING = 1

class Controls:
  LEFT = (K_a, K_LEFT)
  UP = (K_w, K_UP)
  DOWN = (K_s, K_DOWN)
  RIGHT = (K_d, K_RIGHT)
  BOOST = K_SPACE

class Velocity:
  DEFAULT = 1
  FAST = 2
  SUPER_FAST = 4
  SONIC = 10

class FruitTypes:
  DEFAULT = { 'points': 1, 'color': Colors.RED }
  SPECIAL = { 'points': 4, 'color': Colors.YELLOW }