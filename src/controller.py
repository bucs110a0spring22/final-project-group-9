import sys
import pygame
from src import enemy
from src import character
from src import bullet

class Controller:
  def __init__(self, width=640, height=480):
        pygame.init()
        self.score = 0
        self.screen = pygame.display.set_mode((width, height))
        self.bg = pygame.image.load("assets/Background.png")
        self.background = pygame.transform.scale(self.bg, (width, height))
        self.screen.blit(self.background, (0, 0))
        self.bullets = pygame.sprite.Group()
        self.enemy = enemy.Enemy("Alien", 300, 480, "assets/enemyboy.png")
        self.character = character.Character("Spaceboy",100, 100, "assets/spaceboy.png")
        self.bullet = bullet.Bullet("Bullet", self.character.rect.x, self.character.rect.y, "assets/bullet.png", 'ready')
        self.all_sprites = pygame.sprite.Group((self.character), (self.enemy))
        self.state = "GAME"
        num_bullets = 4
        for i in range(num_bullets):
          self.bullets.add(bullet.Bullet("bullet", self.bullet.rect.x, self.bullet.rect.y, "assets/bullet.png", 'ready'))
          



  def mainLoop(self):
    while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
  
  ### below are some sample loop states ###
  #def menuloop(self):
    
      #event loop

      #update data

      #redraw
    
  def gameLoop(self):
    pygame.key.set_repeat(1,1)
    self.image_width = 45
    self.display_width = 640
    while self.state == "GAME":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        
        if event.type == pygame.KEYDOWN:
          if(event.key == pygame.K_LEFT):
            self.character.move_left()
            if self.character.rect.x < 0:
              self.character.rect.x = 0
            elif self.character.rect.x + self.image_width > self.display_width:
              self.character.rect.x = self.display_width - self.image_width
          elif(event.key == pygame.K_RIGHT):
            self.character.move_right()
            if self.character.rect.x > 640:
              self.character.rect.x = 640
            elif self.character.rect.x + self.image_width > self.display_width:
              self.character.rect.x = self.display_width - self.image_width
          elif(event.key == pygame.K_SPACE):
            self.bullets.update(self.screen)
            self.bullet.state = 'ready'
          if(event.key == pygame.K_UP):
            self.character.move_up()
          if(event.key == pygame.K_DOWN):
            self.character.move_down()
            
        #rightwindow = pygame.display(self.character.score)
        #leftwindow = pygame.display(self.character.health)
          
      
            
      #self.enemy.update()
      #self.screen.fill(0,0,0) 
      self.screen.blit(self.background, (0, 0))
      #self.screen.blit(self.bullet.image, (self.bullet.rect.x - 10, self.bullet.rect.y +10))
      self.bullets.draw(self.screen)
      if(self.character.health == 0):
          self.state = "GAMEOVER"
      self.all_sprites.draw(self.screen)
      

            # update the screen
      pygame.display.flip()
     
  def Score(self):
    if self.enemy.kill():
      self.character.score +=1
    
  def gameoverloop(self):
    self.character.kill()
    pygame.font.init()
    myfont = pygame.font.SysFont(None, 30)
    message = myfont.render('Game Over', False, (0, 0, 0))
    self.screen.blit(message, (self.width / 2, self.height / 2))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit()
  
  
    


