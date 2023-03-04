import pygame

from utils import scale_image

# Load the track image
track_img = pygame.image.load('assets/images/track.png')
tire_track_img = scale_image(pygame.image.load('assets/images/car-tire.png'), 0.4)
CAR_IMG = scale_image(pygame.image.load('assets/images/car.png'), 0.4)

# Set up the window
screen_width = track_img.get_width()
screen_height = track_img.get_height()
screen = pygame.display.set_mode((screen_width, screen_height))  # pygame.FULLSCREEN

# static images
images = [(track_img, (0, 0))]

track_surf = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
track_surf.fill((0, 0, 0, 0))