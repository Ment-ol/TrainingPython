from pygame import *
from map import *
import random

init()
window = display.set_mode((580, 800))
hp = 6
music_background = random.randint(1, 5)
# music
if music_background == 1:
    mixer.music.load('res/music_1.mp3')
if music_background == 2:
    mixer.music.load('res/music_2.mp3')
if music_background == 3:
    mixer.music.load('res/music_3.mp3')
if music_background == 4:
    mixer.music.load('res/music_4.mp3')
if music_background == 5:
    mixer.music.load('res/music_5.mp3')

clock = time.Clock()
game = True
mixer.init()

mixer.music.play()
kick = mixer.Sound('res/kick.mp3')
money = mixer.Sound('res/money.mp3')
mixer.music.set_volume(0.20)
kick.set_volume(100)
money.set_volume(0.99)
# transform.scale - змінити розмір
background_image = transform.scale(
    image.load('res/blue.jpg'), (800, 800))


# image.load - заваниажити картинку

class Sprite:

    def __init__(self, image_name, x, y, width, height):
        self.image = transform.scale(
            image.load(image_name), (width, height))
        # автоматично створює хітбокс розмірами з картинку
        self.rect = self.image.get_rect()
        # встановимо кординати!
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def move(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_w]:
            self.rect.y -= 3
        if pressed_keys[K_s]:
            self.rect.y += 3
        if pressed_keys[K_a]:
            self.rect.x -= 3
        if pressed_keys[K_d]:
            self.rect.x += 3

    def auto_move(self, x1, x2):
        if self.rect.x <= x1 or self.rect.x + self.rect.width > x2:
            self.speed *= -1
        self.rect.x += self.speed

    def auto_move_y(self, y1, y2):
        if self.rect.y <= y1 or self.rect.y + self.rect.height > y2:
            self.speed *= -1
        self.rect.y += self.speed

    def is_collide(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def wall_colaide(self, walls):
        pressed_keys = key.get_pressed()
        for wall in walls:
            if self.is_collide(wall):
                if pressed_keys[K_w]:
                    self.rect.y += 3

                if pressed_keys[K_s]:
                    self.rect.y -= 3
                if pressed_keys[K_a]:
                    self.rect.x += 3
                if pressed_keys[K_d]:
                    self.rect.x -= 3

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Sprite('res/dach.jfif', 109, 100, 35, 35)

# squer_enemy = Sprite('res/squer_enemy.png', 55, 427, 51, 51)
squer_enemy1 = Sprite('res/squer_enemy.png', 20, 604, 40, 20)
squer_enemy2 = Sprite('res/squer_enemy.png', 428, 427, 51, 51)
squer_enemy3 = Sprite('res/squer_enemy.png', 428, 50, 51, 51)
squer_enemy4 = Sprite('res/squer_enemy.png', 328, 50, 51, 51)

triangle_enemy = Sprite('res/triangle_enemy1.png', 300, 280, 25, 25)
triangle_enemy1 = Sprite('res/triangle_enemy.png', 118, 128, 30, 30)
triangle_enemy2 = Sprite('res/triangle_enemy3.png', 190, 57, 20, 20)
triangle_enemy3 = Sprite('res/triangle_enemy3.png', 277, 640, 30, 30)
triangle_enemy4 = Sprite('res/triangle_enemy3.png', 277, 290, 30, 30)
triangle_enemy5 = Sprite('res/triangle_enemy3.png', 120, 604, 30, 30)
triangle_enemy6 = Sprite('res/triangle_enemy3.png', 170, 604, 30, 30)

HERT_1 = Sprite('res/blue_hert.png', 50, 5, 35, 35)
HERT_2 = Sprite('res/blue_hert.png', 85, 5, 35, 35)
HERT_3 = Sprite('res/blue_hert.png', 120, 5, 35, 35)
HERT_4 = Sprite('res/blue_hert.png', 155, 5, 35, 35)
HERT_5 = Sprite('res/blue_hert.png', 190, 5, 35, 35)
game_map = make_map()

coin_score = 1
coin_score1 = 1
coin_score2 = 1
coin_score3 = 1
coin_score4 = 1
coin_score5 = 1
coin_score6 = 1
coin_score7 = 1
coin_score8 = 1
coin_score9 = 1
coin_score10 = 1
coin_score11 = 1

coins = Sprite('res/coins.png', 153, 190, 65, 65)
coins1 = Sprite('res/coins.png', 47, 240, 65, 65)
coins2 = Sprite('res/coins.png', 100, 530, 65, 65)
coins3 = Sprite('res/coins.png', 50, 680, 65, 65)
coins4 = Sprite('res/coins.png', 260, 208, 65, 65)
coins5 = Sprite('res/coins.png', 190, 360, 65, 65)
coins6 = Sprite('res/coins.png', 208, 680, 65, 65)
coins7 = Sprite('res/coins.png', 315, 430, 65, 65)
coins8 = Sprite('res/coins.png', 420, 684, 65, 65)
coins9 = Sprite('res/coins.png', 372, 57, 65, 65)
coins10 = Sprite('res/coins.png', 265, 87, 65, 65)
coins11 = Sprite('res/coins.png', 474, 550, 65, 65)
while game:

    window.blit(background_image, (0, 0))
    pressed_keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT or pressed_keys[K_ESCAPE]:
            game = False
    for block in game_map:
        block.draw(window)
    player.move()
    player.wall_colaide(game_map)

    # if player.is_collide(squer_enemy):
    #   kick.play()
    #  player.rect.x = 55
    # player.rect.y = 55
    # hp -= 1
    if player.is_collide(squer_enemy1):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1
    if player.is_collide(squer_enemy2):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1

    if player.is_collide(squer_enemy3):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1
    if player.is_collide(squer_enemy4):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1

    if player.is_collide(triangle_enemy):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1
    if player.is_collide(triangle_enemy1):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1
    if player.is_collide(triangle_enemy2):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1

    if player.is_collide(triangle_enemy3):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1

    if player.is_collide(triangle_enemy4):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1

    if player.is_collide(triangle_enemy5):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1

    if player.is_collide(triangle_enemy6):
        kick.play()
        player.rect.x = 55
        player.rect.y = 55
        hp -= 1

    for block in game_map:
        block.draw(window)

    # 1 МОНЕТА
    if player.is_collide(coins):
        coin_score -= 1

    if coin_score == 1:
        coins.draw()
    if coin_score == 0:
        money.play()

    # 2 МОНЕТА
    if player.is_collide(coins1):
        coin_score1 -= 1
    if coin_score1 == 1:
        coins1.draw()
    if coin_score1 == 0:
        money.play()

    # 3 МОНЕТА
    if player.is_collide(coins2):
        coin_score2 -= 1
    if coin_score2 == 1:
        coins2.draw()
    if coin_score2 == 0:
        money.play()

    # 4 МОНЕТА
    if player.is_collide(coins3):
        coin_score3 -= 1
    if coin_score3 == 1:
        coins3.draw()
    if coin_score3 == 0:
        money.play()

    # 5 МОНЕТА
    if player.is_collide(coins4):
        coin_score4 -= 1
    if coin_score4 == 1:
        coins4.draw()
    if coin_score4 == 0:
        money.play()

    # 6 МОНЕТА
    if player.is_collide(coins5):
        coin_score5 -= 1
    if coin_score5 == 1:
        coins5.draw()
    if coin_score5 == 0:
        money.play()

    # 7 МОНЕТА
    if player.is_collide(coins6):
        coin_score6 -= 1
    if coin_score6 == 1:
        coins6.draw()
    if coin_score6 == 0:
        money.play()

    # 8 МОНЕТА
    if player.is_collide(coins7):
        coin_score7 -= 1
    if coin_score7 == 1:
        coins7.draw()
    if coin_score7 == 0:
        money.play()

    # 9 МОНЕТА
    if player.is_collide(coins8):
        coin_score8 -= 1
    if coin_score8 == 1:
        coins8.draw()
    if coin_score8 == 0:
        money.play()

    # 10 МОНЕТА
    if player.is_collide(coins9):
        coin_score9 -= 1
    if coin_score9 == 1:
        coins9.draw()
    if coin_score9 == 0:
        money.play()

    # 11 МОНЕТА
    if player.is_collide(coins10):
        coin_score10 -= 1
    if coin_score10 == 1:
        coins10.draw()
    if coin_score10 == 0:
        money.play()

    # 12 МОНЕТА
    if player.is_collide(coins11):
        coin_score11 -= 1
    if coin_score11 == 1:
        coins11.draw()
    if coin_score11 == 0:
        money.play()

    for block in game_map:
        block.draw(window)

    # squer_enemy.auto_move(52, 265)
    squer_enemy1.auto_move(0, 110)
    squer_enemy2.auto_move_y(370, 580)
    squer_enemy3.auto_move_y(43, 220)
    squer_enemy4.auto_move_y(43, 220)

    triangle_enemy.auto_move(283, 375)
    triangle_enemy3.auto_move_y(590, 695)
    triangle_enemy4.auto_move_y(270, 375)
    triangle_enemy5.auto_move_y(600, 750)
    triangle_enemy6.auto_move_y(600, 730)

    triangle_enemy.draw()
    triangle_enemy1.draw()
    triangle_enemy2.draw()
    triangle_enemy3.draw()
    triangle_enemy4.draw()
    triangle_enemy5.draw()
    triangle_enemy6.draw()

    player.draw()

    # squer_enemy.draw()
    squer_enemy1.draw()
    squer_enemy2.draw()
    squer_enemy3.draw()
    squer_enemy4.draw()

    if hp == 5:
        HERT_1.draw()
        HERT_2.draw()
        HERT_3.draw()
        HERT_4.draw()
        HERT_5.draw()
    if hp == 4:
        HERT_1.draw()
        HERT_2.draw()
        HERT_3.draw()
        HERT_4.draw()

    if hp == 3:
        HERT_1.draw()
        HERT_2.draw()
        HERT_3.draw()

    if hp == 2:
        HERT_1.draw()
        HERT_2.draw()

    if hp == 1:
        HERT_1.draw()

    if hp == 0:
        text1 = font.SysFont('Listbox', 130).render("YOU LOST", True, (187, 11, 11))
        window.blit(text1, (65, 330))
        display.update()
        time.wait(5000)
        game = False

    if coin_score1 == 0 and coin_score2 == 0 and coin_score3 == 0 and coin_score4 == 0 and coin_score5 == 0 and coin_score6 == 0 and coin_score7 == 0 and coin_score8 == 0 and coin_score9 == 0 and coin_score10 == 0 and coin_score11 == 0:
        text1 = font.SysFont('Listbox', 130).render("YOU WIN", True, (0,0,186))
        window.blit(text1, (65, 330))
        display.update()
        time.wait(5000)
        game = False
    display.update()
    clock.tick(60)
