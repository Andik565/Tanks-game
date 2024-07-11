import pygame as p

# класс взрыв
class Explosion(p.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.images = (
            p.image.load('img/MediumExplosion1.png'),
            p.image.load('img/MediumExplosion2.png'),
            p.image.load('img/MediumExplosion3.png'),
        )
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_rate = 10
        self.last_update = p.time.get_ticks()

    def update(self, *args, **kwargs):
        now = p.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.images):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.images[self.frame]
                self.rect = self.image.get_rect(center=center)



