from pygame import *
# pygame.init()

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
        self.rect.x += speedx
        self.rect.y += speedy
        if self.rect.y >= 700:
            speedy *= -1
        if self.rect.y <= 0:
            speedy *= -1



dybinka = Player('dubinka.png', 10, 400, 20, 80, 100)
dybinka2 = Player('dubinka.png', 1100, 400, 20, 80, 100)
rocket = Ball('byratino.png', 620, 480, 1, 80, 100)
window = display.set_mode((1240, 800))
window.fill((255, 0 ,55))
clock = time.Clock()
run = True
while run:
    window.fill((255, 0 ,55))
    rocket.update()
    rocket.reset()
    dybinka.update()
    dybinka.reset()
    dybinka2.update2()
    dybinka2.reset()
    if sprite.collide_rect(dybinka, rocket) or sprite.collide_rect(dybinka2, rocket) :
        speedx *= -1
    
    for e in event.get():
            if e.type == QUIT:
                run = False
    clock.tick(60)
    display.update()
