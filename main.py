import pygame

from car import Car
from constants import MAX_SPEED, MIN_SPEED, FPS, TURN_SPEED

# Initialize Pygame
pygame.init()

# Load the track image
track_img = pygame.image.load('assets/images/track.png')

# Set up the window
screen_width = track_img.get_width()
screen_height = track_img.get_height()
screen = pygame.display.set_mode((screen_width, screen_height))  # pygame.FULLSCREEN

# Set up the game clock
clock = pygame.time.Clock()


def draw(screen, images, player_car):
    for img, pos in images:
        screen.blit(img, pos)

    player_car.draw(screen)
    pygame.display.update()


def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    elif keys[pygame.K_d]:
        player_car.rotate(right=True)

    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    elif keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()


# static images
images = [(track_img, (0, 0))]

# create car
player_car = Car(MAX_SPEED, MIN_SPEED, TURN_SPEED)

if __name__ == "__main__":
    # Game loop
    while True:

        # update scene
        draw(screen, images, player_car)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Get the keys currently being pressed
        move_player(player_car)

        # Tick the clock
        clock.tick(FPS)
