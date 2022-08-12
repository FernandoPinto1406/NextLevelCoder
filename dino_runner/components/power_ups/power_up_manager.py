import pygame
pygame.mixer.init()
from ...utils.constants import ULTRA_POWER_SOUND

import random
from dino_runner.components.power_ups.hammer import Hammer

from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.set_sound()

    def generate_power_up(self, points):
        if len(self.power_ups) == 0:
            if self.when_appears == points:
                if random.randint(0, 1) == 0:
                    self.when_appears = random.randint(self.when_appears + 150, self.when_appears + 250)
                    self.power_ups.append(Hammer())
                elif random.randint(0, 1) == 1:
                    self.when_appears = random.randint(self.when_appears + 150, self.when_appears + 250)
                    self.power_ups.append(Shield())



    def update(self, points, game_speed, player):
        self.generate_power_up(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True                    
                player.show_text = True
                player.type = power_up.type
                time_random = random.randint(5, 8)
                player.shield_time_up = power_up.start_time + (time_random * 1000)
                self.power_ups.remove(power_up)
                self.sound.play()    
            elif player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.hammer = True
                player.show_text = True
                player.type = power_up.type
                time_random = random.randint(3, 5)
                player.hammer_time_up = power_up.start_time + (time_random * 1000)
                self.power_ups.remove(power_up)
                self.sound.play()    

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)

    def set_sound(self):
        self.sound = pygame.mixer.Sound(ULTRA_POWER_SOUND)
