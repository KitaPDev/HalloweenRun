import os
import pygame

# Global Constants
global SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN, RUNNING, JUMPING, DUCKING, SMALL_SCARECROW, LARGE_SCARECROW, BIRD, CLOUD, BG, GAME_SPEED, POINTS, OBSTACLES, X_POS_BG, Y_POS_BG

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("assets/dino", "DinoRun1.png")),
        pygame.image.load(os.path.join("assets/dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("assets/dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("assets/dino", "DinoDuck1.png")),
        pygame.image.load(os.path.join("assets/dino", "DinoDuck2.png"))]

SMALL_SCARECROW = [pygame.image.load(os.path.join("assets/scarecrow", "SmallScarecrow1.png")),
                pygame.image.load(os.path.join("assets/scarecrow", "SmallScarecrow2.png")),
                pygame.image.load(os.path.join("assets/scarecrow", "SmallScarecrow3.png"))]
LARGE_SCARECROW = [pygame.image.load(os.path.join("assets/scarecrow", "LargeScarecrow1.png")),
                pygame.image.load(os.path.join("assets/scarecrow", "LargeScarecrow2.png")),
                pygame.image.load(os.path.join("assets/scarecrow", "LargeScarecrow3.png"))]

BIRD = [pygame.image.load(os.path.join("assets/bird", "Bird1.png")),
        pygame.image.load(os.path.join("assets/bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("assets/other", "Cloud.png"))

BG = pygame.image.load(os.path.join("assets/other", "Track.png"))

GAME_SPEED = 0
POINTS = 0
OBSTACLES = []
X_POS_BG = 0
Y_POS_BG = 300