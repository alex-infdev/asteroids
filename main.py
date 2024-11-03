import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_triangle = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      return

          player_triangle.update(dt)
          screen.fill("black")
          player_triangle.draw(screen)
          pygame.display.flip()
          dt = clock.tick(60)/1000 #limit the framerate to 60fps


    
if __name__ == "__main__":
        main()


