import os
import pygame

# Global Constants
global SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN, RUNNING, JUMPING, DUCKING, SMALL_PUMPKIN, LARGE_PUMPKIN, WITCH, WITCH_BG, BG, GAME_SPEED, POINTS, OBSTACLES, X_POS_BG, Y_POS_BG

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("assets/mummy", "MummyRun1.png")),
        pygame.image.load(os.path.join("assets/mummy", "MummyRun2.png"))]
JUMPING = pygame.image.load(os.path.join("assets/mummy", "MummyJump.png"))
DUCKING = [pygame.image.load(os.path.join("assets/mummy", "MummyDuck1.png")),
        pygame.image.load(os.path.join("assets/mummy", "MummyDuck2.png"))]

SMALL_PUMPKIN = [pygame.image.load(os.path.join("assets/pumpkin", "SmallPumpkin1.png")),
                pygame.image.load(os.path.join("assets/pumpkin", "SmallPumpkin2.png")),
                pygame.image.load(os.path.join("assets/pumpkin", "SmallPumpkin3.png"))]
LARGE_PUMPKIN = [pygame.image.load(os.path.join("assets/pumpkin", "LargePumpkin1.png")),
                pygame.image.load(os.path.join("assets/pumpkin", "LargePumpkin2.png")),
                pygame.image.load(os.path.join("assets/pumpkin", "LargePumpkin3.png"))]

WITCH = [pygame.image.load(os.path.join("assets/witch", "Witch1.png")),
        pygame.image.load(os.path.join("assets/witch", "Witch2.png"))]

WITCH_BG = pygame.image.load(os.path.join("assets/other", "Witch.png"))

BG = pygame.image.load(os.path.join("assets/other", "Track.png"))

GAME_SPEED = 0
POINTS = 0
OBSTACLES = []
X_POS_BG = 0
Y_POS_BG = 360