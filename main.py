import pygame
import random
from mummy import Mummy
from witch_bg import WitchBG
from obstacle_factory import ObstacleFactory
import settings as s

pygame.init()
pygame.display.set_caption("Halloween Run")

def main():
    run = True
    clock = pygame.time.Clock()
    
    player = Mummy()
    witchBg = WitchBG()

    s.GAME_SPEED = 20
    s.X_POS_BG = 0
    s.Y_POS_BG = 0
    s.POINTS = 0
    s.OBSTACLES = []
    
    font = pygame.font.Font('freesansbold.ttf', 20)
    death_count = 0

    def score():
        s.POINTS += 1
        if s.POINTS % 100 == 0:
            s.GAME_SPEED += 2

        text = font.render(str(s.POINTS), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        s.SCREEN.blit(text, textRect)

    def background():
        image_width = s.BG.get_width()
        s.SCREEN.blit(s.BG, (s.X_POS_BG, s.Y_POS_BG))
        s.SCREEN.blit(s.BG, (image_width + s.X_POS_BG, s.Y_POS_BG))
        if s.X_POS_BG <= -image_width:
            s.SCREEN.blit(s.BG, (image_width + s.X_POS_BG, s.Y_POS_BG))
            s.X_POS_BG = 0
        s.X_POS_BG -= s.GAME_SPEED

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()

        s.SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        background()

        if len(s.OBSTACLES) == 0:
            s.OBSTACLES.append(ObstacleFactory.create(random.randint(0, 2)))

        for obs in s.OBSTACLES:
            if pygame.sprite.collide_rect(player, obs):
                player.draw(s.SCREEN)
                player.update(userInput)
                obs.draw(s.SCREEN)
                obs.update()
                pygame.time.delay(1500)
                death_count += 1
                menu(death_count)

            obs.draw(s.SCREEN)
            obs.update()

        player.draw(s.SCREEN)
        player.update(userInput)

        witchBg.draw(s.SCREEN)
        witchBg.update()

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        s.SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(s.POINTS), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (s.SCREEN_WIDTH // 2, s.SCREEN_HEIGHT // 2 + 50)
            s.SCREEN.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (s.SCREEN_WIDTH // 2, s.SCREEN_HEIGHT // 2)
        s.SCREEN.blit(text, textRect)
        s.SCREEN.blit(s.RUNNING[0], (s.SCREEN_WIDTH // 2 - 50, s.SCREEN_HEIGHT // 2 - 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)