import pygame
import constants
import random
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

def generate_shape_queue():
    shape_queue = random.sample(constants.SHAPES_COLORS, len(constants.SHAPES_COLORS))
    return shape_queue
