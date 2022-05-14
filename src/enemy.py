import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image):
      super().__init__()
      self.img = pygame.image.load('assets/enemyboy.png')
      self.image = pygame.transform.scale(self.img, (50, 50))
      self.rect = self.image.get_rect()
      self.rect.x = 200 
      self.rect.y = 200
      self.speed = 1
      self.health = 1

def update(self):
    if self.rect.y > 2:
       self.rect.y -= 1
    elif self.rect.y < 0:
         self.rect.y += 1