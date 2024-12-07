import pygame
from Tile import Tile

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))  # Adjusted to 800x800 for a square board
        self.grid_cells = []
        self.tile_size = 80

    def start_game(self):

        for i in range(8):  # row
            for j in range(8):  # column
                color = (238,238,210) if (i + j) % 2 == 0 else (118,150,86)
                self.grid_cells.append(Tile(j * self.tile_size + 100, i * self.tile_size + 100, self.tile_size, self.tile_size, color))

        running = True

        while running:
            self.screen.fill((49, 46, 43))  # Fill the screen before drawing tiles

            for tile in self.grid_cells:
                tile.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

        pygame.quit()