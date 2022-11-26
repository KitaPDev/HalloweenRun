import pygame
import settings

class Mummy:
    X_POS = 80
    Y_POS = 340
    Y_POS_DUCK = 380
    JUMP_VEL = 8.5

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Mummy, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.duck_img = settings.DUCKING
        self.run_img = settings.RUNNING
        self.jump_img = settings.JUMPING

        self.mummy_duck = False
        self.mummy_run = True
        self.mummy_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]

        rect = self.image.get_bounding_rect()
        c = rect.center
        w = rect.width * 0.25
        h = rect.height * 0.25
        new_rect = pygame.Rect(0,0,w,h)
        new_rect.center = c

        self.rect = new_rect
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, userInput, isDead = False):
        if self.mummy_duck:
            self.duck()
        if self.mummy_run:
            self.run()
        if self.mummy_jump:
            self.jump()
        if isDead:
            self.dead()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.mummy_jump:
            self.mummy_duck = False
            self.mummy_run = False
            self.mummy_jump = True
        elif userInput[pygame.K_DOWN] and not self.mummy_jump:
            self.mummy_duck = True
            self.mummy_run = False
            self.mummy_jump = False
        elif not (self.mummy_jump or userInput[pygame.K_DOWN]):
            self.mummy_duck = False
            self.mummy_run = True
            self.mummy_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.rect = self.image.get_bounding_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.rect = self.image.get_bounding_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.mummy_jump:
            self.rect.y -= self.jump_vel * 5
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.mummy_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
