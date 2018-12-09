import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        deneme = self.player.pos.y + self.player.rect.y / 2
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        #print("Current pos: ", self.player.pos)
        if hits:
            if self.player.vel.y > 0:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
            if self.player.vel.y < 0:
                differenceY = self.player.pos.y - hits[0].rect.bottom
                if 10 > differenceY > 0:
                    print("collide")
                    self.player.pos.y = self.player.pos.y + self.player.rect.height + hits[0].rect.height * 2
                    self.player.vel.y = PLAYER_GRAV

            print(self.player.acc)
            if self.player.acc.x > 0:
                differenceX = self.player.pos.x - hits[0].rect.centerx
                print(differenceX)
                if 20 > differenceX > 0:
                    self.player.acc.x = 0
                # if self.player.vel.y > 0:
        #     hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        #     if hits:
        #         self.player.pos.y = hits[0].rect.top
        #         self.player.vel.y = 0
        # if self.player.vel.y < 0:
        #     hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        #     if hits:
        #         self.player.pos.y = hits[0].rect.bottom - deneme
        #         self.player.vel.y = PLAYER_GRAV

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()