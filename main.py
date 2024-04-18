from pygame import *
# pygame.init()
font.init()
speedx = -1
speedy = -1
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 640:
            self.rect.y += self.speed 
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 640:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        global speedx
        global speedy
        global live1, live2
        self.rect.x += speedx
        self.rect.y += speedy
        if self.rect.y >= 700:
            speedy *= -1
        if self.rect.y <= 0:
            speedy *= -1



live1 = 3
live2 = 3
final = False
dybinka = Player('dubinka.png', 10, 400, 20, 80, 100)
dybinka2 = Player('dubinka.png', 1100, 400, 20, 80, 100)
rocket = Ball('byratino.png', 620, 480, 1, 80, 100)
window = display.set_mode((1240, 800))
window.fill((255, 0 ,55))
clock = time.Clock()
run = True
font1 = font.SysFont('verdana', 70)
font2 = font.SysFont('verdana', 40)
text_live1 = font2.render(str(live1), 1, (0, 0, 255))
text_live2 = font2.render(str(live2),  1, (0, 0, 255))

while run:
    if final != True:
        window.fill((255, 0 ,55))
        window.blit(text_live2, (1200, 10))
        window.blit(text_live1, (10, 10))
        rocket.update()
        rocket.reset()
        dybinka.update()
        dybinka.reset()
        dybinka2.update2()
        dybinka2.reset()
        if rocket.rect.x >= 1240:
            live2 -= 1
            print(live1, live2)
            text_live2 = font2.render(str(live2), 1, (0, 0, 255))
            window.blit(text_live2, (1200, 10))
        if live2 <= 0:

            text_lose = font1.render('Проиграл второй', 1, (0, 0, 255))
            window.blit(text_lose, (500, 200))
            final = True
        if rocket.rect.x <= 0:
            live1 -= 1
            print(live1, live2)
            text_live1 = font2.render(str(live1), 1, (0, 0, 255))
            window.blit(text_live1, (10, 10))
        if live1 <= 0:
            text_lose = font1.render('Проиграл первый', 1, (0, 0, 255))
            window.blit(text_lose, (500, 200))
            final = True
        if sprite.collide_rect(dybinka, rocket) or sprite.collide_rect(dybinka2, rocket) :
            speedx *= -1
    
    for e in event.get():
            if e.type == QUIT:
                run = False
    clock.tick(60)
    display.update()
