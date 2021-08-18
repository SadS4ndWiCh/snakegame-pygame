import pygame

import random

from src.entity import Entity
from src.interfaces import FruitTypes
from src.utils import random_grid_pos

from constants import TILE_SIZE

class Fruit(Entity):
  def __init__(self):
    self.position = pygame.Vector2()
    self.fruit_type = FruitTypes.DEFAULT

    self.new_position()

  def get_points(self) -> int:
    """ Retorna a quantidade de pontos que o tipo da frutinha dá """

    return self.fruit_type['points']

  def get_color(self) -> list[int]:
    """ Retorna a cor do tipo da frutinha """
    
    return self.fruit_type['color']

  def reset_fruit(self):
    """ Define uma nova posição aleatória para a frutinha """

    new_position = random_grid_pos(True)
    self.position.x = new_position.x
    self.position.y = new_position.y

    # 5% de chance de ser uma fruta especial
    if(random.random() <= 0.05):
      self.fruit_type = FruitTypes.SPECIAL
    
    else:
      self.fruit_type = FruitTypes.DEFAULT

  def draw(self, screen: pygame.Surface):
    """ Desenha a frutinha na tela """

    fruit_rect = pygame.Rect(
      self.position.x * TILE_SIZE,
      self.position.y * TILE_SIZE,
      TILE_SIZE,
      TILE_SIZE
    )
    pygame.draw.rect(screen, self.get_color(), fruit_rect)