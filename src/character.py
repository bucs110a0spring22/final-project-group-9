import pygame

class Character(pygame.sprite.Sprite):
  
    def __init__(self, name, x, y, image):
      super().__init__()
      self.image = pygame.image.load('assets/spaceboy.png').convert_alpha()
      self.rect = self.image.get_rect()
      self.rect.x = 20
      self.rect.y = 100
      self.speed = 5
      self.health = 3
      self.direction = 'R'
      #self.screen = pygame.display.set_mode(800, 600)
    
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

    def fights(self, asteroid, enemy):
      fights = pygame.sprite.spritecollide(self.hero, self.enemy, True)
      if(fights):
        for enemy in fights:
          if(self.hero.fights(enemy)):
            enemy.kill()
            self.score += 1
            print(self.score)
          else:
            self.enemy.add(enemy)
            print(self.score)
    def Character(self, screen):
      screen.blit(self.image, (self.rect.x, self.rect.y))
  