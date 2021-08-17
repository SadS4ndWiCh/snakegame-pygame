import pygame

import time
from typing import Union

from src.snake import Snake
from src.fruit import Fruit
from src.interfaces import GameStates, Controls, Colors

from constants import WIDTH, HEIGHT

class Game():
  def __init__(self, title: str) -> None:
    self.game_state = GameStates.RUNNING
    self.screen: Union[pygame.Surface, None] = None

    #            Left   Up     Down   Right  Space
    self.keys = [False, False, False, False, False]
    self.player = Snake()
    self.fruit = Fruit()

    self.score = 0
    self.max_score = 0

    self.__previous_frame_time = 0
    self.__dt = 0
    self.__elapsed_time = 0

    self.__setup_pygame(title)

  def __calcule_deltatime(self):
    """ Calcula o Deltatime """

    self.__dt = time.time() - self.__previous_frame_time
    self.__dt *= 60
    self.__previous_frame_time = time.time()

  def __setup_pygame(self, title: str):
    """ Inicializa o Pygame """
    
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(title)

    pygame.init()

  def reset_game(self):
    """ Finaliza o jogo e reseta para as configurações iniciais """

    self.keys = [False, False, False, False, False]

    self.max_score = max(self.score, self.max_score)

    print(f'Pontuação final de {self.score} pontos!')
    print(f'Seu record foi de {self.max_score}')
    
    self.score = 0

    self.__previous_frame_time = 0
    self.__dt = 0
    self.__elapsed_time = 0

    self.player.reset_snake()
    self.fruit.new_position()

  def handle_inputs(self, event):
    """ Manipula os inputs do usuário """

    if event.type == pygame.KEYDOWN:
      if event.key in Controls.LEFT: self.keys[0] = True
      elif event.key in Controls.UP: self.keys[1] = True
      elif event.key in Controls.DOWN: self.keys[2] = True
      elif event.key in Controls.RIGHT: self.keys[3] = True
      elif event.key == Controls.BOOST: self.keys[4] = True

    if event.type == pygame.KEYUP:
      if event.key in Controls.LEFT: self.keys[0] = False
      elif event.key in Controls.UP: self.keys[1] = False
      elif event.key in Controls.DOWN: self.keys[2] = False
      elif event.key in Controls.RIGHT: self.keys[3] = False
      elif event.key == Controls.BOOST: self.keys[4] = False

  def handle_events(self):
    """ Manipula os eventos do jogo """

    for event in pygame.event.get():
      if(event.type == pygame.QUIT):
        self.game_state = 2

      self.handle_inputs(event)

  def update(self):
    """ Função responsável por conter os updates do jogo """

    self.handle_events()
    self.__calcule_deltatime()

    self.__elapsed_time += self.__dt

    if(self.__elapsed_time > (5 / self.player.velocity)):
      self.player.move(self.keys, self.__dt)
      if(self.player.check_if_self_collide()):
        self.reset_game()
      
      else:
        self.player.update_body()

        if(self.player.has_collide(self.fruit)):
          self.player.increase_body(self.fruit.get_points())
          self.fruit.new_position()
          self.score += 1

        self.__elapsed_time = 0

  def render(self):
    """ Função responsável por conter as renderizações do jogo """

    self.screen.fill(Colors.BLACK)

    self.player.draw(self.screen)
    self.fruit.draw(self.screen)

    pygame.display.update()

  def run(self):
    """ Roda o jogo """

    while(self.game_state == GameStates.RUNNING):
      self.update()
      self.render()