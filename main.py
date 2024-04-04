from pygame import *
# pygame.init()
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
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 595:
            self.rect.x += self.speed 
dybinka = Player('dubinka.png', 10, 400, 20, 80, 100)
rocket = Player('byratino.png', 620, 480, 20, 80, 100)
window = display.set_mode((1240, 960))
window.fill((255, 0 ,55))
clock = time.Clock()
run = True
while run:
    rocket.reset()
    dybinka.reset()
    for e in event.get():
            if e.type == QUIT:
                run = False
    clock.tick(60)
    display.update()
