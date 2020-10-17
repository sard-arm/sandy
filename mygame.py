import pygame
pygame.init()
width = 640
height = 480
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("MyGame")
class Player(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
class Wall(pygame.sprite.Sprite):
    def __init__(self, color, x, y,width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player = pygame.transform.scale(pygame.image.load("sprites/statue1_angry.png"), (40,40))
start_x = 100
start_y = 310
walls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
totem = Player(player, start_x, start_y, 1)
Wall1 = Wall(pygame.Color("orange"), 100,300,400,10)
Wall2 = Wall(pygame.Color("orange"), 500,250,10,100)
Wall3 = Wall(pygame.Color("orange"), 200,150,400,10)
Wall4 = Wall(pygame.Color("orange"), 500,90,400,10)
Wall5 = Wall(pygame.Color("orange"), 450,300,300,10)
Wall6 = Wall(pygame.Color("orange"), 365,69,400,10)
Wall7 = Wall(pygame.Color("orange"), 226,96,345,10)
walls.add(Wall1)
walls.add(Wall2)
walls.add(Wall3)
walls.add(Wall4)
walls.add(Wall5)
walls.add(Wall6)
walls.add(WAll7)
all_sprites.add(totem)
all_sprites.add(Wall1)
all_sprites.add(Wall2)
all_sprites.add(Wall3)
all_sprites.add(Wall4)
all_sprites.add(Wall5)
all_sprites.add(Wall6)
all_sprites.add(Wall7)


run = True
while run:
    pygame.time.delay(30)
    window.fill(pygame.Color("red"))


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    if e.type == pygame.KEYDOWN:
        if keys[pygame.K_a] and totem.rect.x > 0:
            totem.rect.x -= totem.speed
        if keys[pygame.K_d] and totem.rect.x < width-32:
            totem.rect.x += totem.speed
        if keys[pygame.K_w] and totem.rect.y >0:
            totem.rect.y -= totem.speed 
        if keys[pygame.K_s] and totem.rect.y < height-32:
            totem.rect.y += totem.speed
    if len(pygame.sprite.pygame.sprite.spritecollide(totem, walls, False)) > 0:
        totem.rect.x = start_x
        totem.rect.y = start_y

    keys = pygame.key.get_pressed()
    all_sprites.update()
    all_sprites.draw(window)    
    pygame.display.update()

    


