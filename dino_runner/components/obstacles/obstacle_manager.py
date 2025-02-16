
import random
import pygame

from dino_runner.components.obstacles.small_cactus import SmallCactus
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import BIRD, DIE_SOUND, SMALL_CACTUS, LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.set_sound_dying()

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
               self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
               self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
               self.obstacles.append(Bird(BIRD))            

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:             
                   self.sound.play()
                   pygame.time.delay(500)
                   game.playing  = False
                   game.death_count += 1
                else:
                    self.obstacles.remove(obstacle)
                break
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []

    def set_sound_dying(self):
        self.sound = pygame.mixer.Sound(DIE_SOUND)
