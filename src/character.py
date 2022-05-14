import pygame

class Character(pygame.sprite.Sprite):
  
    def __init__(self, name, x, y, image):
      pygame.sprite.Sprite.__init__(self)
      self.img = pygame.image.load('assets/spaceboy.png')
      self.image = pygame.transform.scale(self.img, (70, 70))
      self.rect = self.image.get_rect()
      self.rect.x = 320
      self.rect.y = 320
      self.image_width = 45
      self.display_width = 640
      self.speed = 1
      self.health = 3
      self.score = 0
    
    
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

            