import pygame
from src import character
class Bullet(pygame.sprite.Sprite):

  def __init__(self, limit):
    super().__init__()
    self.image = pygame.image.load('assets/8-bit-Bullet.png').convert_alpha()
    self.rect = self.image.get_rect()  # rectangle
    self.rect.x = 0
    self.rect.y = character.y
    self.rect.xchange = 0
    self.rect.ychange = 10
    self.limit = limit
    self.speed = 10

    def fire_bullet(self):
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN():
          if event.key == pygame.K_SPACE:
            self.screen.blit(self.image, (character.x,character.y))
            Bullet.rect.y = character.y + self.rect.ychange
      
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed

    
        if self.rect.x > self.limit:
          self.kill()