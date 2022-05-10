import pygame

class Bullet(pygame.sprite.Sprite):

  def __init__(self, limit):
    super().__init__()
    self.image = pygame.image.load('assets/8-bit-Bullet.png').convert_alpha()
    self.rect = self.image.get_rect()  # rectangle
    self.limit = limit
    self.speed = 10

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed

        if self.rect.x > self.limit:
          self.kill()