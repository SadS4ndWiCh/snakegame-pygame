from pygame import Vector2

from abc import ABC, abstractmethod

class Entity(ABC):
  def __init__(self) -> None:
    self.position = Vector2()

  def has_collide(self, other):
    """ Checa se a entidade se colidiu com outra """

    if(not issubclass(type(other), Entity)):
      raise ValueError('É necessário que a classe seja do tipo Entity')

    return self.position == other.position

  @abstractmethod
  def draw(self):
    ...