import pygame
import sys
import random

pygame.init()

screen_width = 600
screen_height = 600
block_size = 40

font = pygame.font.SysFont("Bauharus 93", 40)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Real Snake")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = block_size, block_size
        self.xdir = 1           #if xdir == 1 means we are moving right; if is -1, then we are moving left
        self.ydir = 0           #if ydir == 1, moving down; if -1, moving up
        self.head = pygame.Rect(self.x, self.y, block_size, block_size) 
        self.body = [pygame.Rect(self.x - block_size, self.y, block_size, block_size)]
        self.dead = False
        self.stop = False    

    def update(self):
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True



        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * block_size
        self.head.y += self.ydir * block_size        
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, screen_width)/ block_size) * block_size
        self.y = int(random.randint(0, screen_height)/ block_size) * block_size
        self.rect = pygame.Rect(self.x, self.y, block_size, block_size)
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)


def draw_grid():
    for x in range(0, screen_width, block_size):
        for y in range(0, screen_height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, "grey", rect, 1)

snake = Snake()
apple = Apple()
draw_grid()


serpentine = True
while serpentine:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0 
            elif event.key == pygame.K_RIGHT:
                snake.xdir = 1
                snake.ydir = 0
            elif event.key == pygame.K_LEFT:
                snake.xdir = -1
                snake.ydir = 0        
            elif event.key == pygame.K_1:
                snake.stop = True           

    snake.update()

    screen.fill("black")
    draw_grid()
    
    apple.update()

    #draw snake's head.
    pygame.draw.rect(screen, "grey", snake.head)

    #draw snake's body.
    for square in snake.body:
        pygame.draw.rect(screen, "yellow", square)

    #check if the head of the snake meets the position of the apple
    if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.body.append(pygame.Rect(square.x, square.y, block_size, block_size))
            apple = Apple()
    
    pygame.display.update()
    clock.tick(5)        
    
    
    
    
    
    
    
    


