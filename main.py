import pygame
from src import controller


def main():
  main_window = controller.Controller()
  main_window.mainLoop()
main()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/