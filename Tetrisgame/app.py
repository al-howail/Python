import pygame
import random



pygame.init()
screen_width = 300
screen_height = 600
block_size = 30
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')


colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255)
]



shapes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]



def create_grid():
    return [[0 for _ in range(10)] for _ in range(20)]



def draw_grid(screen, grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(screen, colors[grid[y][x]], (x * block_size, y * block_size, block_size, block_size))



def draw_shape(screen, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, colors[cell], (off_x + x * block_size, off_y + y * block_size, block_size, block_size))


def valid_space(shape, grid, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + off_x < 0 or x + off_x >= len(grid[0]) or y + off_y >= len(grid) or grid[y + off_y][x + off_x]:
                    return False
    return True


def drop_shape(shape, grid, offset):
    new_offset = (offset[0], offset[1] + 1)
    if not valid_space(shape, grid, new_offset):
        return offset, False
    return new_offset, True


def join_grid(shape, grid, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + off_y][x + off_x] = cell
    return grid


def main():
    clock = pygame.time.Clock()
    grid = create_grid()
    current_shape = random.choice(shapes)
    shape_pos = [3, 0]  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_pos = (shape_pos[0] - 1, shape_pos[1])
                    if valid_space(current_shape, grid, new_pos):
                        shape_pos = new_pos
                if event.key == pygame.K_RIGHT:
                    new_pos = (shape_pos[0] + 1, shape_pos[1])
                    if valid_space(current_shape, grid, new_pos):
                        shape_pos = new_pos
                if event.key == pygame.K_DOWN:
                    shape_pos, success = drop_shape(current_shape, grid, shape_pos)
                    if not success:
                        grid = join_grid(current_shape, grid, shape_pos)
                        current_shape = random.choice(shapes)
                        shape_pos = [3, 0]

        shape_pos, success = drop_shape(current_shape, grid, shape_pos)
        if not success:
            grid = join_grid(current_shape, grid, shape_pos)
            current_shape = random.choice(shapes)
            shape_pos = [3, 0]

        screen.fill((0, 0, 0))
        draw_grid(screen, grid)
        draw_shape(screen, current_shape, shape_pos)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
