import pygame
import random

pygame.init()

WINDOW_SIZE = 600
CELL_SIZE = WINDOW_SIZE // 10
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("10x10 White Grid")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SNAKE_COLOUR = (0, 255, 0)
SNAKE2_COLOUR = (255, 0, 0)
FOOD_COLOUR = (0, 0, 255)

snake = [[1, 1], [2, 1], [3, 1]]
snake2 = [[9, 9], [8, 9], [7, 9]]
direction = [0, 0]
direction2 = [0, 0]
food = [5, 5]
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = [0, -1]
            elif event.key == pygame.K_s:
                direction = [0, 1]
            elif event.key == pygame.K_a:
                direction = [-1, 0]
            elif event.key == pygame.K_d:
                direction = [1, 0]
            elif event.key == pygame.K_UP:
                direction2 = [0, -1]
            elif event.key == pygame.K_DOWN:
                direction2 = [0, 1]
            elif event.key == pygame.K_LEFT:
                direction2 = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                direction2 = [1, 0]
    
    if direction != [0, 0]:
        head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        if 0 <= head[0] <= 9 and 0 <= head[1] <= 9 and head not in snake and head not in snake2:
            snake.insert(0, head)
            if head == food:
                food = [random.randint(0, 9), random.randint(0, 9)]
                while food in snake or food in snake2:
                    food = [random.randint(0, 9), random.randint(0, 9)]
            else:
                snake.pop()
    
    if direction2 != [0, 0]:
        head2 = [snake2[0][0] + direction2[0], snake2[0][1] + direction2[1]]
        if 0 <= head2[0] <= 9 and 0 <= head2[1] <= 9 and head2 not in snake and head2 not in snake2:
            snake2.insert(0, head2)
            if head2 == food:
                food = [random.randint(0, 9), random.randint(0, 9)]
                while food in snake or food in snake2:
                    food = [random.randint(0, 9), random.randint(0, 9)]
            else:
                snake2.pop()
    
    screen.fill(BLACK)
    
    for i in range(11):
        pygame.draw.line(screen, WHITE, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), 1)
        pygame.draw.line(screen, WHITE, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), 1)
    
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOUR, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    for segment in snake2:
        pygame.draw.rect(screen, SNAKE2_COLOUR, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, FOOD_COLOUR, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.display.flip()
    clock.tick(10)

def draw_snake():
    pygame.draw.rect(screen, SNAKE_COLOUR, (1 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def move_snake():
    pass

def check_collision():
    pass

def check_food():
    pass

def check_game_over():
    pass

pygame.quit()
