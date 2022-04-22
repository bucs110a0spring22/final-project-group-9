from src import player, utility

class Enemy(player.Player):

    def fight(self, opponent):
        pass

    def update(self):
        if self.rect.y > utility.Utility.screen_height:
            self.rect.y -= 1
        elif self.rect.y < 0:
            self.rect.y += 1