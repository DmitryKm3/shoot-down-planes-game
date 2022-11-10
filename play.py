import pygame
from gun import Gun
#Variables
wight, height = 800, 800 #screen size
FPS = 60 #FPS
#game name
pygame.display.set_caption("Самолеты")
#main function
def main():
    pygame.init()
    window = pygame.display.set_mode((wight, height))
    gun = Gun(window)
    clock = pygame.time.Clock()
#event cycle
    Run = True
    while Run:
        for event in pygame.event.get():
            #exit from the program
            if event.type == pygame.QUIT:
                Run = False
            elif event.type == pygame.KEYDOWN:
            #shooting
                if event.key == pygame.K_SPACE:
                    print("ff")
        #right and left movement
        keys = pygame.key.get_pressed()
        #movement to the left
        if keys[pygame.K_LEFT] and gun.rect_image.x > 0:
            gun.rect_image.x -= gun.speed
        #movement to the right
        if keys[pygame.K_RIGHT] and wight - gun.g_wight > gun.rect_image.x:
            gun.rect_image.x += gun.speed



        clock.tick(FPS)
        window.fill('black')
        gun.start()
        pygame.display.flip()

main()
