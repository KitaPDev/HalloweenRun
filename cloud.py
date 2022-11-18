import random
import settings

class Cloud:
    def __init__(self):
        self.x = settings.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = settings.CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= settings.GAME_SPEED
        if self.x < -self.width:
            self.x = settings.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
