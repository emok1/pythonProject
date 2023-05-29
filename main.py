import pygame

pygame.init()
win = pygame. display.set_mode((1900,1050))

pygame.display.set_caption("ты не уйдеш ")

x=50
y=50
x1=400
y1=400
w=50
h=50
speed= 20
ani=1
pygame.mixer.music.load('myzika/mp3.mp3')
pygame.mixer.music.play()
i= 0
fon = pygame.image.load('img1/fon.jpg')
ahha = pygame.image.load('img1/haha.png')
gg = pygame.image.load('img1/gg (2).png')
ptica = [
    pygame.image.load('img1/1.png'),
    pygame.image.load('img1/2.png'),
    pygame.image.load('img1/3.png'),
    pygame.image.load('img1/4.png'),
    pygame.image.load('img1/5.png'),
]


def drawWindow():
    global i
    if i < 4:
        i += 1
    else:
        i= 0

    win.blit(fon, (-20,-530))
    if ani==1:
        win.blit(ahha,(x1,y1))
    if ani==2:
        win.blit(gg, (x1, y1))
    win.blit(ptica[i],(x,y))

    pygame.display.update()

run= True
while run:
    pygame.time.delay(78)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and y<1050-h:
        y+= speed
    if keys[pygame.K_UP]and y>0:
        y-= speed
    if keys[pygame.K_LEFT]and x>0:
        x-= speed
    if keys[pygame.K_RIGHT]and x<1900-w:
        x+= speed

    if keys[pygame.K_s]:
        y1+= speed
    if keys[pygame.K_w] :
        y1-= speed
    if keys[pygame.K_a]:
        ani=2
        x1-= speed
    if keys[pygame.K_d]:
        ani=1
        x1+= speed

    drawWindow()



pygame.quit()