import random
import settings
import pygame

class ObstacleFactory():
    def __init__():
        pass

    def create(obsTypeId):
        if obsTypeId == 0:
            return SmallPumpkin(settings.SMALL_PUMPKIN)
        elif obsTypeId == 1:
            return LargePumpkin(settings.LARGE_PUMPKIN)
        elif obsTypeId == 2:
            return Witch(settings.WITCH)

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type

        rect = self.image[self.type].get_bounding_rect()
        c = rect.center
        w = rect.width * 0.6
        h = rect.height * 0.4
        new_rect = pygame.Rect(0,0,w,h)
        new_rect.center = c

        self.rect = new_rect
        self.rect.x = settings.SCREEN_WIDTH

    def update(self):
        self.rect.x -= settings.GAME_SPEED
        if self.rect.x < -self.rect.width:
            settings.OBSTACLES.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallPumpkin(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 420


class LargePumpkin(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 390


class Witch(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 220 + (random.randint(0, 1) * 140)
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1