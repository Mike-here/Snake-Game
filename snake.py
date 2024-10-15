import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
block_size = 50

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


def draw_grid():
    for x in range(0, screen_width, block_size):
        for y in range(0, screen_height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, "green", rect, 1)

snake = Snake()

draw_grid()


serpentine = True
while serpentine:

    #draw snake's head.
    pygame.draw.rect(screen, "red", snake.head)

    #draw snake's body.
    for square in snake.body:
        pygame.draw.rect(screen, "red", square)
    
    
    
    
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit


    pygame.display.update()
    clock.tick(10)        
