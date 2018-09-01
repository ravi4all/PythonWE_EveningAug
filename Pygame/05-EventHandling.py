import pygame

pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))

color_1 = 105,180,200
red = 155,0,0

x = 0
y = 0
moveX = 0
moveY = 0

game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            # print(event)
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

        # elif event.type == pygame.KEYUP:
        #     moveX = 0
        #     moveY = 0

    screen.fill(color_1)
    pygame.draw.rect(screen, red, [x,y,50,50])

    x += moveX
    y += moveY

    if x > width:
        x = -50
    elif x < -50:
        x = width

    elif y > height:
        y = -50
    elif y < -50:
        y = height

    pygame.display.update()