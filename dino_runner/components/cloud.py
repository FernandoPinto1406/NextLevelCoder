from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD, CLOUD_TYPE, SCREEN_WIDTH

class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.type = CLOUD_TYPE
        self.rect.y = 150
        self.rect.x = SCREEN_WIDTH
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH


    def update(self, game_speed, clouds):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            clouds.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)