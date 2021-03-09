import pygame


class Ball:
    def __init__(self, pos, color):
        self.pos = pos  # (100, 100)
        self.color = color
        self.rorate = True
        pygame.draw.circle(screen, self.color, self.pos, 50)

    def hmove(self):
        if self.pos[0] == 50:
            self.rorate = False
        elif self.pos[0] == 1030:
            self.rorate = True
        if self.rorate:
            self.pos = (self.pos[0] - 1, self.pos[1])
        else:
            self.pos = (self.pos[0] + 1, self.pos[1])

    def renew(self):
        pygame.draw.circle(screen, self.color, self.pos, 50)


pygame.init()
FPS = 240
screen = pygame.display.set_mode((1080, 520))
clock = pygame.time.Clock()
balls = []
x, y = 50, 200
screen.fill((255, 0, 0))
rorate = True
running = True
stop = False
ball = ''
r, g, b = 90, 39, 44
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ball = Ball((x, y), (0, 255, 0))
                balls.append(ball)
            if event.button == 3:
                del balls[0]
    screen.fill((255, 0, 0))
    for i in balls:
        i.renew()
        i.hmove()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
