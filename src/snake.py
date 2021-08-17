import pygame

import math

from src.entity import Entity
from src.interfaces import MoveDirection, Colors, Velocity
from src.utils import random_grid_pos

from constants import WIDTH, HEIGHT, TILE_SIZE

class Snake(Entity):
  def __init__(self) -> None:
    self.size = pygame.Vector2(TILE_SIZE, TILE_SIZE)
    self.position = pygame.Vector2()
    self.velocity = Velocity.DEFAULT
    self.move_direction = MoveDirection.RIGHT
    
    self.body: list[pygame.Vector2] = []
    self.min_body_size = 3
    self.max_body_size = 3

    self.random_snake_position()
    self.update_body()

  def reset_snake(self):
    """ Reseta a cobra para as configurações padrões """

    self.velocity = 1
    self.move_direction = MoveDirection.RIGHT

    self.body = []
    self.min_body_size = 3
    self.max_body_size = 3

    self.random_snake_position()
    self.update_body()

  def check_if_self_collide(self) -> bool:
    """ Checa se a cobra colidiu com seu próprio corpo """

    for body_ind, body_part in enumerate(self.body):
      if(body_ind == len(self.body) - 1): continue

      if(body_part == self.position): return True
    
    return False

  def random_snake_position(self):
    """ Define uma posição aleatória para a cobra """

    random_position = random_grid_pos(True)
    self.position.x = random_position.x
    self.position.y = random_position.y

  def increase_body(self, amount: int):
    """ Aumenta o tamanho máximo do corpo da cobrinha """

    self.max_body_size += amount

  def update_body(self):
    """ Atualiza colocando uma nova posição do corpo e removendo quando for maior que o máximo """

    body_length = len(self.body)
    self.body.append(pygame.Vector2(self.position))

    while(
      body_length > math.floor(self.max_body_size) and body_length > self.min_body_size
    ):
      self.body = self.body[1:]
      body_length = len(self.body)

  def move(self, keys: list[bool], dt: float):
    """ Move a cobrinha com base na direção """

    moves = {
      MoveDirection.LEFT: [-1, 0], # Left
      MoveDirection.UP: [0, -1], # Up
      MoveDirection.DOWN: [0, 1], # Down
      MoveDirection.RIGHT: [1, 0], # Right
    }

    [isLeft, isUp, isDown, isRight, isBoost] = keys
    current_move = moves[self.move_direction]
    
    if(True in keys):
      next_direction = MoveDirection.LEFT if isLeft else \
                  MoveDirection.UP if isUp else \
                  MoveDirection.DOWN if isDown else \
                  MoveDirection.RIGHT if isRight else None
      
      if(next_direction != None):
        next_move = moves[next_direction]

        move_dx = current_move[0] + next_move[0]
        move_dy = current_move[1] + next_move[1]

        if([move_dx, move_dy] != [0, 0]):
          self.move_direction = next_direction

    if(isBoost and len(self.body) > self.min_body_size):
      print(len(self.body), self.min_body_size)

      self.velocity = Velocity.FAST
      self.max_body_size -= 0.5

    else: self.velocity = Velocity.DEFAULT

    self.position.x += current_move[0] * self.size.x
    self.position.y += current_move[1] * self.size.y

    if(self.position.x < 0): self.position.x = WIDTH
    elif(self.position.x > WIDTH): self.position.x = 0

    if(self.position.y < 0): self.position.y = HEIGHT
    elif(self.position.y > HEIGHT): self.position.y = 0

  def draw(self, screen: pygame.Surface):
    """ Desenha a cobrinha na tela """

    for body_ind, body_part in enumerate(self.body):
      body_rect = pygame.Rect(body_part.x, body_part.y, self.size.x, self.size.y)
      color = Colors.color_by_hue(body_ind / len(self.body))

      pygame.draw.rect(screen, color, body_rect)
