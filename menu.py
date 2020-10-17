def start_menu():
    import pygame
    from gametest import play
    pygame.init() # инициализируем pygame
    

    width = 640 # задаем ширину окна
    height = 500 # задаем высоту окна
    window = pygame.display.set_mode((width, height)) # создаем игровое окно
    pygame.display.set_caption("MyGame") # задаем заголовок окну
    pygame.display.set_icon(pygame.image.load("item_skull.ico"))

    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 30)
    label_text = font1.render("MyGame", True, pygame.Color("white"))
    space_text = font1.render("Нажмите ПРОБЕЛ для начала игры", True, pygame.Color("white"))
    uprav_text = font2.render("Упрвление: W,A,S,D or l,r,u,d",True, pygame.Color("grey"))
    story_text2 = font2.render("сундук с сокровищами! ",True, pygame.Color("grey"))
    story_text = font2.render("Соберите все монеты,пройдя множесво испытаний и заберите ",True, pygame.Color("grey"))
    bg = pygame.transform.scale(pygame.image.load("Desert.png"), (width,height))
    run = True # флаг цикла игры
    while run:
        pygame.time.delay(5) # задержка экрана
        window.blit(bg,(0,0))

        # проверяем выход из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # запоминаем нажатые клавиши в keys
        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                play()
                break
                  
        window.blit(label_text, (32, 32))
        window.blit(space_text, (100, 100))
        window.blit(uprav_text, (32,180))
        window.blit(story_text, (0,260))
        window.blit(story_text2, (170,340))
        pygame.display.update()

start_menu()
