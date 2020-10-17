def play():
    import pygame
    from menu import start_menu
    import pygame.mixer
    pygame.init()
    width = 700
    height = 700
    points = 0
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Sandy")
    pygame.display.set_icon(pygame.image.load("item_skull.ico"))

    pygame.mixer.music.load("Sounds/Mario.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    #classes
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

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, img, x, y,speed):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = speed
            
    class Coin(pygame.sprite.Sprite):
        def __init__(self, img, x, y,):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
    
    class Chest(pygame.sprite.Sprite):
        def __init__(self, img, x, y,):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    font = pygame.font.Font(None,35)
    coins_text = font.render("Монеты:0", True, pygame.Color("grey"))
    font2 = pygame.font.Font(None,60)
    win_text = font2.render("YOU WIN!!!", True, pygame.Color("red"))
    space_text = font.render("Нажмите ПРОБЕЛ для выхода в меню",True, pygame.Color("white"))
    font2 = pygame.font.Font(None,22)
    upral_text = font2.render("Упрвление: W,A,S,D or l,r,u,d",True, pygame.Color("black"))
    story_text = font2.render("Соберите все монетыбпройдя множесво испытаний и заберите ",True, pygame.Color("black"))
    story_text2 = font2.render("сундук с сокровищами! ",True, pygame.Color("black"))
    #constants
    size = 40
    line_width = 15
    #Transformation
    player = pygame.transform.scale(pygame.image.load("player2.png"), (size,size))
    bg = pygame.transform.scale(pygame.image.load("Desert.png"), (width,height))
    enemy = pygame.transform.scale(pygame.image.load("player.png"), (size,size))
    coin = pygame.transform.scale(pygame.image.load("coin1.png"), (size,size))
    chest = pygame.transform.scale(pygame.image.load("chest_lock_open.png"), (size,size))
    #Start Location
    start_x = line_width
    start_y = line_width
    
    start_x2 = line_width*10
    start_y2 = size*6
    
    start_x3 = line_width*15
    start_y3 = size*6
    
    start_x4 = line_width*20
    start_y4 = size*6
    
    start_x5 = line_width*6
    start_y5 = size
    
    start_x6 = line_width*6
    start_y6 = size*2+line_width*2
    
    start_x7 = line_width*2
    start_y7 = size+line_width+size+line_width+size+line_width*3+line_width+size+size+size
    
    start_x8 = line_width*2
    start_y8 = size+size+line_width+size+line_width+size+line_width*3+line_width+size+size+size
    
    start_x9 = line_width*2
    start_y9 = line_width+size+line_width+size+line_width*3+line_width+size+size+size
    
    start_x10 = line_width*2
    start_y10 = line_width+line_width+size+line_width*3+line_width+size+size+size
    
    start_x11 = size*7
    start_y11 = size+line_width+size+line_width+size+line_width*4+size+line_width+size+size+size+line_width+size*4

    #the basis
    walls = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    chests = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    totem = Player(player, start_x, start_y, 5)
    enemy1 = Enemy(enemy, start_x2, start_y2, 9)
    enemy2 = Enemy(enemy, start_x3, start_y3, 2)
    enemy3 = Enemy(enemy, start_x4, start_y4, 5)
    coin1 = Coin(coin, start_x5, start_y5)
    coin2 = Coin(coin, start_x6, start_y6)
    coin3 = Coin(coin, start_x7, start_y7)  
    coin4 = Coin(coin, start_x8, start_y8)
    coin5 = Coin(coin, start_x9, start_y9)
    coin6 = Coin(coin, start_x10, start_y10)
    chest = Chest(chest, start_x11, start_y11)
    #the formation of
    Wall1 = Wall(pygame.Color("orange"), 0,0,width,line_width)
    Wall2 = Wall(pygame.Color("orange"), 0,0,line_width,height)
    Wall3 = Wall(pygame.Color("orange"), 0,height-line_width,width,line_width)
    Wall4 = Wall(pygame.Color("orange"), width-line_width,0,line_width,height)
    Wall5 = Wall(pygame.Color("orange"), 0,size+line_width*2,width-size-line_width*2,line_width)
    Wall6 = Wall(pygame.Color("orange"), size+line_width*2,size+size+line_width*4,width-size,line_width)
    Wall7 = Wall(pygame.Color("orange"), 0,line_width+size+size+line_width*2+line_width+size+line_width*2,width-size-line_width*2,line_width)
    Wall8 = Wall(pygame.Color("orange"), size+line_width*3,size+line_width*3+size+line_width+size+line_width*4+size+line_width+size+size+size+line_width,width-size+line_width*2,line_width)
    Wall9 = Wall(pygame.Color("yellow"), line_width,size+line_width+size+line_width+line_width+size+line_width+size+line_width*4+size+line_width+size+size+line_width,size+line_width*2,line_width)
    #HitBox
    walls.add(Wall1)
    walls.add(Wall2)
    walls.add(Wall3)
    walls.add(Wall4)
    walls.add(Wall5)
    walls.add(Wall6)
    walls.add(Wall7)
    walls.add(Wall8)
    #walls.add(Wall9)
    enemies.add(enemy1)
    enemies.add(enemy2)
    enemies.add(enemy2)
    coins.add(coin1)
    coins.add(coin2)
    coins.add(coin3)
    coins.add(coin4)
    coins.add(coin5)
    coins.add(coin6)
    #revitalization
    all_sprites.add(totem)
    all_sprites.add(enemy1)
    all_sprites.add(enemy2)
    all_sprites.add(enemy3)
    all_sprites.add(Wall1)
    all_sprites.add(Wall2)
    all_sprites.add(Wall3)
    all_sprites.add(Wall4)
    all_sprites.add(Wall5)
    all_sprites.add(Wall6)
    all_sprites.add(Wall7)
    all_sprites.add(Wall8)
    all_sprites.add(Wall9)
    all_sprites.add(coin1)
    all_sprites.add(coin2)
    all_sprites.add(coin3)
    all_sprites.add(coin4)
    all_sprites.add(coin5)
    all_sprites.add(coin6)
    
    #
    font = pygame.font.Font(None,35)
    coins_text = font.render("Монеты:0", True, pygame.Color("grey"))
    #cycle
    run = True
    while run:
        pygame.time.delay(30)
        window.blit(bg,(0,0))
    #Touch Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        enemy1.rect.y += enemy1.speed
        enemy2.rect.y += enemy2.speed
        enemy3.rect.y += enemy3.speed
        if event.type == pygame.KEYDOWN:
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and totem.rect.x > 0:
                totem.rect.x -= totem.speed
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and totem.rect.x < width-32:
                totem.rect.x += totem.speed
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and totem.rect.y >0:
                totem.rect.y -= totem.speed 
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and totem.rect.y < height-32:
                totem.rect.y += totem.speed


    #Death treatment       
        if len(pygame.sprite.pygame.sprite.spritecollide(totem, walls, False)) > 0:
            totem.rect.x = start_x
            totem.rect.y = start_y

        if len(pygame.sprite.pygame.sprite.spritecollide(totem, enemies, False)) > 0:
            totem.rect.x = start_x
            totem.rect.y = start_y
        if len(pygame.sprite.pygame.sprite.spritecollide(enemy1, walls, False)) > 0:
            enemy1.speed *= -1
        if len(pygame.sprite.pygame.sprite.spritecollide(enemy2, walls, False)) > 0:
            enemy2.speed *= -1
        if len(pygame.sprite.pygame.sprite.spritecollide(enemy3, walls, False)) > 0:
            enemy3.speed *= -1
        if len(pygame.sprite.pygame.sprite.spritecollide(totem, coins, True)) > 0:
            points += 1
            coins_text = font.render(("Монеты:0" + str(points)), True, pygame.Color("yellow"))
        window.blit(coins_text, (550, 650))
        #if len(pygame.sprite.pygame.sprite.spritecollide(totem, coins, True)) > 0:
           # points == 4
        if points == 6:
            chests.add(chest)
            all_sprites.add(chest)
        if len(pygame.sprite.pygame.sprite.spritecollide(totem, chests, False)) > 0:
            break
    #Driving mechanism
        keys = pygame.key.get_pressed()
        all_sprites.update()
        all_sprites.draw(window)    
        pygame.display.update()
    #2display
    while run:
        window.fill(pygame.Color("black"))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                start_menu()
                break
        window.blit(space_text, (90,420))
        window.blit(win_text, (230,320))
        pygame.display.update()
