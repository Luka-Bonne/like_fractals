import pygame
import random
import time
import os


A = (600, 100)
B = (350, 500)
C = (850, 500)

pygame.init()
size = width, height = 900, 600
screen = pygame.display.set_mode(size)

button_group = pygame.sprite.Group()
circles_group = pygame.sprite.Group()
circle_group = pygame.sprite.Group()

white = pygame.Color('#FDFDFD')
purple = pygame.Color('#CABBE9')
blue = pygame.Color('#A1EAFB')
pink = pygame.Color('#FFCEF3')
screen.fill(white)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image

MUSIC = pygame.mixer.Sound('data\\light.wav')

BUTTONS = {'play': load_image('play.png'),
           'pause': load_image('pause.png'),
           'replay': load_image('replay.png'),
           'acceleration': load_image('acceleration.png')}

w_btn = 50
h_btn = 50


class Button(pygame.sprite.Sprite):
    def __init__(self, what):
        super().__init__(button_group)
        self.image = BUTTONS[what]
        self.status = what
        if what == 'play':
            self.rect = self.image.get_rect().move(150, 200)
        elif what == 'replay':
            self.rect = self.image.get_rect().move(50, 200)
        elif what == 'pause':
            self.rect = self.image.get_rect().move(50, 350)
        elif what == 'acceleration':
            self.rect = self.image.get_rect().move(150, 350)
        self.width = w_btn
        self.height = h_btn


class Circles(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__(circles_group)
        self.image = pygame.Surface((12, 12), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pink, (6, 6), 6, 0)
        self.coords = coords
        self.rect = self.image.get_rect()
        self.rect.center = self.coords


class Circle(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__(circle_group)
        self.image = pygame.Surface((12, 12), pygame.SRCALPHA)
        pygame.draw.circle(self.image, blue, (6, 6), 6, 0)
        self.coords = coords
        self.rect = self.image.get_rect()
        self.rect.center = self.coords


def starting_circles():
    pygame.draw.circle(screen, purple, A, 8, 0)
    pygame.draw.circle(screen, purple, B, 8, 0)
    pygame.draw.circle(screen, purple, C, 8, 0)


def start_circle(coords):
    circle_group.empty()
    Circle(coords)


def play(n, c):
    if n == 1:
        x = (A[0] - c[0]) // 2
        y = (A[1] - c[1]) // 2
        coords = (c[0] + x, c[1] + y)
        Circles(coords)
        start_circle(coords)
    elif n == 2:
        x = (B[0] - c[0]) // 2
        y = (B[1] - c[1]) // 2
        coords = (c[0] + x, c[1] + y)
        Circles(coords)
        start_circle(coords)
    elif n == 3:
        x = (C[0] - c[0]) // 2
        y = (C[1] - c[1]) // 2
        coords = (c[0] + x, c[1] + y)
        Circles(coords)
        start_circle(coords)
    return coords


def pause(x):
    pass


def accel(c):
    n = random.choice(a)
    if n == 1:
        x = (A[0] - c[0]) // 2
        y = (A[1] - c[1]) // 2
        coords = (c[0] + x, c[1] + y)
        Circles(coords)
        start_circle(coords)
    elif n == 2:
        x = (B[0] - c[0]) // 2
        y = (B[1] - c[1]) // 2
        coords = (c[0] + x, c[1] + y)
        Circles(coords)
        start_circle(coords)
    elif n == 3:
        x = (C[0] - c[0]) // 2
        y = (C[1] - c[1]) // 2
        coords = (c[0] + x, c[1] + y)
        Circles(coords)
        start_circle(coords)
    return coords


fps = 100
clock = pygame.time.Clock()

pygame.mixer.Sound.play(MUSIC)

font = pygame.font.Font(None, 30)
text_A = font.render("A", 1, pygame.Color('#000000'))
text_B = font.render("B", 1, pygame.Color('#000000'))
text_C = font.render("C", 1, pygame.Color('#000000'))

font1 = pygame.font.Font(None, 20)
txt_s = font1.render("Точка", 1, pygame.Color('#000000'))
txt_r = font1.render("Заново", 1, pygame.Color('#000000'))
txt_p = font1.render("Стоп", 1, pygame.Color('#000000'))
txt_a = font1.render("Ускорить", 1, pygame.Color('#000000'))

font2 = pygame.font.Font(None, 10)
txt = font2.render("Я тут", 1, pygame.Color('#000000'))

Button('play')
Button('pause')
Button('replay')
Button('acceleration')

a = [1, 2, 3]
f = False
c = (random.randint(350, 800), random.randint(50, 550))
while c == A or c == B or c == C:
    c = (random.randint(350, 800), random.randint(50, 550))
Circles(c)
start_circle(c)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 150 < mouse[0] < 200 and 200 < mouse[1] < 250:
                c = play(random.choice(a), c)
                #play 150, 200
            elif 50 < mouse[0] < 100 and 200 < mouse[1] < 250:
                c = (random.randint(350, 800), random.randint(50, 550))
                while c == A or c == B or c == C:
                    c = (random.randint(350, 800), random.randint(50, 550))
                circle_group.empty()
                circles_group.empty()
                f = False
                Circles(c)
                start_circle(c)
                #replay 50, 200
            elif 50 < mouse[0] < 100 and 350 < mouse[1] < 400:
                f = False
                #pause 50, 350
            elif 150 < mouse[0] < 200 and 350 < mouse[1] < 400:
                f = True
                #a... 150, 350
    if f:
        c = accel(c)

    screen.fill(white)
    button_group.draw(screen)
    circles_group.draw(screen)
    circle_group.draw(screen)
    starting_circles()

    screen.blit(txt_s, (c[0] + 10, c[1] - 5))

    screen.blit(text_A, (A[0] - 7, A[1] - 30))
    screen.blit(text_B, (B[0] - 6, B[1] + 10))
    screen.blit(text_C, (C[0] - 6, C[1] + 10))

    screen.blit(txt_s, (150 + 5, 200 - 20))
    screen.blit(txt_r, (50, 200 - 20))
    screen.blit(txt_p, (50 + 8, 350 + 50))
    screen.blit(txt_a, (150 - 6, 350 + 50))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()