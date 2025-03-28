from code.Const import ENTITY_SPEED
from code.entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple, number: int):
        super().__init__(name, position)
        self.number = number

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]