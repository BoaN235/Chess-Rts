import pygame
from Tile import Tile

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))  # Adjusted to 800x800 for a square board
        self.grid_cells = []
        self.tile_size = 80

        # Load chess piece images
        self.pieces = {
            'white_pawn': pygame.image.load('icons/pawn-w.svg'),
            'white_rook': pygame.image.load('icons/rook-w.svg'),
            'white_knight': pygame.image.load('icons/knight-w.svg'),
            'white_bishop': pygame.image.load('icons/bishop-w.svg'),
            'white_queen': pygame.image.load('icons/queen-w.svg'),
            'white_king': pygame.image.load('icons/king-w.svg'),
            'black_pawn': pygame.image.load('icons/pawn-b.svg'),
            'black_rook': pygame.image.load('icons/rook-b.svg'),
            'black_knight': pygame.image.load('icons/knight-b.svg'),
            'black_bishop': pygame.image.load('icons/bishop-b.svg'),
            'black_queen': pygame.image.load('icons/queen-b.svg'),
            'black_king': pygame.image.load('icons/king-b.svg'),
        }

        # Scale images to fit the tile size
        for key in self.pieces:
            self.pieces[key] = pygame.transform.scale(self.pieces[key], (self.tile_size*2, self.tile_size*2))

    def start_game(self):
        for i in range(8):  # row
            for j in range(8):  # column
                color = (238, 238, 210) if (i + j) % 2 == 0 else (118, 150, 86)
                self.grid_cells.append(Tile(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size, color))

        running = True

        while running:
            self.screen.fill((49, 46, 43))  # Fill the screen before drawing tiles

            for tile in self.grid_cells:
                tile.draw(self.screen)

            # Draw chess pieces on the board
            for i in range(8):
                for j in range(8):
                    if i == 1:
                        self.screen.blit(self.pieces['black_pawn'], (j * self.tile_size, i * self.tile_size))
                    elif i == 6:
                        self.screen.blit(self.pieces['white_pawn'], (j * self.tile_size, i * self.tile_size))
                    elif i == 0:
                        if j == 0 or j == 7:
                            self.screen.blit(self.pieces['black_rook'], (j * self.tile_size, i * self.tile_size))
                        elif j == 1 or j == 6:
                            self.screen.blit(self.pieces['black_knight'], (j * self.tile_size, i * self.tile_size))
                        elif j == 2 or j == 5:
                            self.screen.blit(self.pieces['black_bishop'], (j * self.tile_size, i * self.tile_size))
                        elif j == 3:
                            self.screen.blit(self.pieces['black_queen'], (j * self.tile_size, i * self.tile_size))
                        elif j == 4:
                            self.screen.blit(self.pieces['black_king'], (j * self.tile_size, i * self.tile_size))
                    elif i == 7:
                        if j == 0 or j == 7:
                            self.screen.blit(self.pieces['white_rook'], (j * self.tile_size, i * self.tile_size))
                        elif j == 1 or j == 6:
                            self.screen.blit(self.pieces['white_knight'], (j * self.tile_size, i * self.tile_size))
                        elif j == 2 or j == 5:
                            self.screen.blit(self.pieces['white_bishop'], (j * self.tile_size, i * self.tile_size))
                        elif j == 3:
                            self.screen.blit(self.pieces['white_queen'], (j * self.tile_size, i * self.tile_size))
                        elif j == 4:
                            self.screen.blit(self.pieces['white_king'], (j * self.tile_size, i * self.tile_size))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

        pygame.quit()