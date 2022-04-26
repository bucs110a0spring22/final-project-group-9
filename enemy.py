from src import player, utility

class Enemy(player.Player):

    def fight(self, opponent):
        pass

    def update(self):
        if self.rect.y > utility.Utility.screen_height:
            self.rect.y -= 1
        elif self.rect.y < 0:
            self.rect.y += 1



#enemy1 ufo that periodically appears and fires a bulets downward. Does not move. Dies in one hit.
#enemy2 an alien that appears on screen but doesnt move initially for 3 seconds. After the 3 seconds it starts to home in on the player. The player gets hit by the alien it loses health. 