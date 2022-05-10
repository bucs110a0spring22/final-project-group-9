import sys
import pygame
import random
from src import enemy
from src import character
#from src import bullet
from src import asteroid

class Controller:
  from src import character
  def __init__(self, width=640, height=480):
        pygame.init()
        self.score = 0
        self.screen = pygame.display.set_mode((640, 480))
        self.background = pygame.image.load("assets/Background.png")
        self.screen.blit(self.background, (0, 0))
        self.enemy = enemy.Enemy("Alien", 80, 50, "assets/Ufo.png")
        self.enemy = pygame.sprite.Group()
        num_enemy = 5
        for i in range(num_enemy):
            x = random.randrange(50, 600)
            y = 400
            self.enemy.add(asteroid.Asteroid("Asteroid", x, y,       
            "assets/Asteroid.png"))
        self.hero = character.Character("Spaceboy", 300, 400, "assets/spaceboy.png")
        self.all_sprites = pygame.sprite.Group((self.hero), tuple(self.enemy))
        self.state = "GAME"
    
    
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
    while self.state == "GAME":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if(event.key == pygame.K_UP):
            self.character.move_up()
          elif(event.key == pygame.K_DOWN):
            self.character.move_down()
          elif(event.key == pygame.K_LEFT):
            self.character.move_left()
          elif(event.key == pygame.K_RIGHT):
            self.character.move_right()
        
      
            
      self.enemy.update()
      #self.screen.fill(0,0,0) 
      self.screen.blit(self.background, (0, 0))
      if(self.hero.health == 0):
          self.state = "GAMEOVER"
      self.all_sprites.draw(self.screen)

            # update the screen
      pygame.display.flip()
     # character()
    
  def gameoverloop(self):
    self.hero.kill()
    pygame.font.init()
    myfont = pygame.font.SysFont(None, 30)
    message = myfont.render('Game Over', False, (0, 0, 0))
    self.screen.blit(message, (self.width / 2, self.height / 2))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit()
  
#  def playermovement(self,event,screen,x,y):
#    if event.type == pygame.KEYDOWN:
#          if(event.key == pygame.K_UP):
#            self.character.move_up()
#          elif(event.key == pygame.K_DOWN):
#            self.character.move_down()
#          elif(event.key == pygame.K_LEFT):
#            self.character.move_left()
#          elif(event.key == pygame.K_RIGHT):
#            self.character.move_right()
#    screen.blit(self.hero, (x,y))
  
    


#write code for the scoring process. You blow up an asteroid you get 1 point. shoot a ufo you get 5 points. you shoot a homing alien you get 8 points. The score should appear at the top right side of the screen.

#write code for the health system in the game. The health will appear on the top left. The spaceship starts off with 3 health after getting hit by anything the spaceship loses 1 health.