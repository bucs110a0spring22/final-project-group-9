import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image):
      super().__init__()
      self.image = pygame.image.load('assets/Ufo.png')
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y

    def update(self):
        if self.rect.y > 2:
            self.rect.y -= 1
        elif self.rect.y < 0:
            self.rect.y += 1