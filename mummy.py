import pygame
import settings

class Mummy:
    X_POS = 80
    Y_POS = 340
    Y_POS_DUCK = 380
    JUMP_VEL = 8.5

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Mummy, self).__new__(self)
        return self.instance

    def __init__(self):
        self.duck_img = settings.DUCKING
        self.run_img = settings.RUNNING
        self.jump_img = settings.JUMPING

        self.is_ducking = False
        self.is_running = True
        self.is_jumping = False

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

    def update(self, userInput):
        if self.is_ducking:
            self.duck()
        if self.is_running:
            self.run()
        if self.is_jumping:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.is_jumping:
            self.is_ducking = False
            self.is_running = False
            self.is_jumping = True
        elif userInput[pygame.K_DOWN] and not self.is_jumping:
            self.is_ducking = True
            self.is_running = False
            self.is_jumping = False
        elif not (self.is_jumping or userInput[pygame.K_DOWN]):
            self.is_ducking = False
            self.is_running = True
            self.is_jumping = False

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
        if self.is_jumping:
            self.rect.y -= self.jump_vel * 5
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.is_jumping = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
