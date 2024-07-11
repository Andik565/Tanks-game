import time

import pygame
import random

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [
            pygame.image.load('img/img_1.png'),
            pygame.image.load('img/img.png'),
            pygame.image.load('img/img_2.png'),
        ]
        self.img_index = random.randint(0, 2)
        self.image = self.images[self.img_index]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - self.image.get_width())
        self.rect.y = random.randint(0, 600 - self.image.get_height())
        self.lifetime = 10
        self.createtime = time.time()

    def update(self, *args, **kwargs):
        if time.time() - self.createtime >= self.lifetime:
            self.kill()