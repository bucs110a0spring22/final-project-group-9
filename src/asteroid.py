import pygame
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, name, x=0, y=0, filenames=None):
      super().__init__()
      self.image = pygame.image.load('assets/Asteroid.png')
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.name = name + str(id(self))
      self.speed = 1
      self.health = 1
      self.rect.y += self.speed
        
    
    def update(self):
      if self.kill():
        self.speed += 1

          