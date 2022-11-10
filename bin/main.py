import pygame
from colors import Color
from scene import Menu, Gameover
from game import Game

class Main:

    def __init__(self, sizex, sizey, title):

        pygame.init()
        pygame.mixer.init()
        # Especificar uma musica que fique tocando durante o jogo
        # pygame.mixer.music.load("assets/sounds/bg.ogg")
        # pygame.mixer.music.play(-1)

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)
        self.icon = pygame.image.load('assets/ico.png')
        pygame.display.set_icon(self.icon)

        # self.menu = Menu("assets/start.png")
        # self.game = Game()
        # self.gameover = Gameover("assets/gameover.png")
        self.height = sizey
        self.width = sizex 

        self.fps = pygame.time.Clock()
        self.loop = True

        # Cores
        self.color = Color()

    # Cenas / Telas
    def draw(self):
        self.window.fill(self.color.lavender)
    # Cada cena tem uma variavel chamada "change_scene" valor False
    # Tela do Menu / Press Start 
        # if not self.menu.change_scene:
        #     self.menu.draw(self.window)
    # O jogo   
        # elif not self.game.change_scene:
        #     self.game.draw(self.window)
        #     self.game.update()
    # Game Over
        # elif not self.gameover.change_scene:
        #     self.gameover.draw(self.window)
    # Reset game
        # else: 
        #     self.game.change_scene = False
        #     self.gameover.change_scene = False
        #     self.game.bee.life = 3
        #     self.game.bee.pts = 0
        #     self.game.bee.sprite.rect[1] = 550

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            # if not self.menu.change_scene:
            #     self.menu.events(events)
            # elif not self.game.change_scene:
            #     self.game.bee.move_bee(events) 
            # else:
            #     self.gameover.events(events) 

    def update(self):
        while self.loop:
            # Controle de FPS
            self.fps.tick(30) 
            self.draw()
            self.events()
            pygame.display.update()

x = 360
y = 640
company = "Zodia Games"
gamename = "Flappy Bird"
play = Main(x, y, f'{company} | {gamename}')
play.update()
