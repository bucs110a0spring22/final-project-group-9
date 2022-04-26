import pygame
import random

class Character(pygame.sprite.Sprite):

  def __init__(self, x=0, y=0, filenames=None):
    super()
    self.image_set = [pygame.image.load(file_name) for f in filenames]
    self.current_image = 0
    self.image = self.image_set[self.current_image]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

  def move(self,direction):
    if direction == "Left":
      self.rect.x = self.rect.y - 1
    elif direction == "Right":
      self.rect.x = self.rect.y + 1
    #elif direction == "LEFT":
      #self.rect.x = self.rect.x - 1
    #elif direction == "RIGHT":
      #self.rect.x = self.rect.x + 1

  def fight(self, opponent):
        return random.randrange(3)
        # res = random.randrange(3)
        # if res:
        #     return True
        # else:
        #     return False
    #required by pygame if inheriting from the sprite
    #update for actions that are not based on events 
    def update():   
        self.current_image = (self.current_image + 1) % len(self.image_set)
        self.image = self.image_set[self.current_image]

