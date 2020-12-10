import pygame, sys

def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((500,400),0, 23)

    WHITE = (255,255,255)
    BLUE = (0,0,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY, BLUE, (200,150,100,50))

    while True:
        for event in pygame.event.get():
            if event.type == quit:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()


