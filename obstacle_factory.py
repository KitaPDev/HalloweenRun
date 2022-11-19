import random
import settings

class ObstacleFactory():
    def __init__():
        pass

    def create(obsTypeId):
        if obsTypeId == 0:
            return SmallScarecrow(settings.SMALL_SCARECROW)
        elif obsTypeId == 1:
            return LargeScarecrow(settings.LARGE_SCARECROW)
        elif obsTypeId == 2:
            return Bird(settings.BIRD)

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_bounding_rect()
        self.rect.x = settings.SCREEN_WIDTH

    def update(self):
        self.rect.x -= settings.GAME_SPEED
        if self.rect.x < -self.rect.width:
            settings.OBSTACLES.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallScarecrow(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeScarecrow(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250 + (random.randint(0, 1) * 30)
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1