import pygame

class Bullet(pygame.sprite.Sprite):

  def __init__(self, limit, x, y, image, state):
    super().__init__()
    self.img = pygame.image.load('assets/bullet.png')
    self.image = pygame.transform.scale(self.img, (70, 70))
    self.rect = self.image.get_rect()
    self.bullets = []
    self.rect.x = x
    self.rect.y = y
    self.x = x
    self.y = y
    self.limit = limit
    self.speed = 10
    self.state = state
    
  def update(self, screen):
          
          self.rect.x = self.x
          self.rect.y = self.y
          self.rect.y -= self.speed  
          