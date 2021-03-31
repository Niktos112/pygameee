import pygame

pygame.init()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 30
        self.board=[[0]*(self.height//self.cell_size) for i in range(self.width//self.cell_size)]
        self.board[0][0] = 0
        print(self.board)
        self.move = 1

    def render(self):
        x, y = 0, 0
        for i in range(self.height//self.cell_size):
            for j in range(self.width//self.cell_size):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)
                elif self.board[i][j] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size))
                    pygame.draw.line(screen,(0, 0, 0), (x, y), (x + self.cell_size, y + self.cell_size), 1)
                    pygame.draw.line(screen, (0, 0, 0), (x + self.cell_size, y), (x, y + self.cell_size), 1)
                elif self.board[i][j] == 2:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size))
                    pygame.draw.circle(screen, (255, 0, 0), (x + self.cell_size // 2, y + self.cell_size // 2), self.cell_size // 2)
                x += self.cell_size
            y += self.cell_size
            x = 0

    def on_click(self, x, y):
        if self.move == 1:
            self.board[x//self.cell_size][y//self.cell_size] = 1
            self.move = 2
        elif self.move == 2:
            self.board[x//self.cell_size][y//self.cell_size] = 2
            self.move = 1

    def check(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1 or self.board[i][j] == 2:
                    if self.board[i][j] == 1:
                        if j != 0:
                            if self.board[i][j - 1] == 1 and self.board[i][j + 1] == 1:
                                pass
                        else:
                            if j == len(self.board[i]) - 1:
                                if self.board[i][j - 1]

x, y = 170, 230
screen = pygame.display.set_mode((x, y))
main_board = Board(1000, 1000)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            main_board.on_click(event.pos[1], event.pos[0])
    screen.fill((0, 0, 0))
    main_board.render()
    pygame.display.flip()
