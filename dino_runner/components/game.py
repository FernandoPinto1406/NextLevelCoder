from winsound import PlaySound
import pygame
pygame.mixer.init()

from dino_runner.components.get_message import get_message

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

from dino_runner.utils.constants import BG, DIE_SOUND, DINO_START, ICON, POINT_SOUND, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.set_sound_score()


        self.points = 0 
        self.death_count = 0


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.game_speed = 20
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
       
    def update_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.sound.play()
            self.game_speed +=1

    def set_sound_score(self):
         self.sound = pygame.mixer.Sound(POINT_SOUND)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.player.check_invincibility(self.screen)       
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        get_message(
            screen = self.screen,
            screen_width = 1000,
            screen_height = 50,
            what_message=(f"Points: {self.points}"),
            size = 22)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                
            if event.type == pygame.KEYDOWN:
                self.points=0
                self.run()
                
    def show_menu(self):
        self.screen.fill((255, 255, 000))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
          get_message(
            screen = self.screen,
            screen_width = half_screen_width, 
            screen_height = half_screen_height + 110,
            what_message=("Press any key to start"),
            size = 30)
        elif self.death_count > 0:
          get_message(
            screen = self.screen,
            screen_width = half_screen_width, 
            screen_height = half_screen_height + 90,
            what_message=("Press any key to Restart"),
            size = 35)
          get_message(
            screen = self.screen,
            screen_width = half_screen_width, 
            screen_height = half_screen_height + 150,
            what_message=(f"Your  score: {self.points}"),
            size = 25)
          
          get_message(
            screen = self.screen,
            screen_width = half_screen_width, 
            screen_height = half_screen_height + 180,
            what_message=(f"Your  number of tries: {self.death_count}"),
            size = 25)            
        self.screen.blit(DINO_START, (half_screen_width - 250, half_screen_height - 150))
        
        pygame.display.update()
        self.handle_key_events_on_menu()

  