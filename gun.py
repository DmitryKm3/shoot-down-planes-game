import pygame

class Gun():
    def __init__(self, window):
        self.window = window
        self.g_wight, self.g_heingt = 70, 70
        self.speed = 10
        self.image = pygame.image.load('gun.png')
        self.rect_image = self.image.get_rect()
        self.rect_image.x = 370
        self.rect_image.y = 730
        self.image_small = pygame.transform.scale(self.image, (self.g_wight, self.g_heingt))


    def start(self):
        self.window.blit(self.image_small, self.rect_image)