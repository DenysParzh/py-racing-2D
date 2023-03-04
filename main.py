import pygame

from constants import MAX_SPEED, MIN_SPEED, FPS, TURN_SPEED
from loader import screen, images
from car import Car


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


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the game clock
    clock = pygame.time.Clock()

    # create car
    player_car = Car(MAX_SPEED, MIN_SPEED, TURN_SPEED)

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


if __name__ == "__main__":
    main()
