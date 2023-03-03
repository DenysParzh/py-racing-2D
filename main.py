import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the car image
car_img = pygame.image.load('assets/images/car.png')
track_img = pygame.image.load('assets/images/track.png')
# Set up the car's initial position, speed and angle
car_x = screen_width // 2
car_y = screen_height // 2
car_speed = 0
car_angle = 0

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Get the keys currently being pressed
    keys = pygame.key.get_pressed()

    # Update the car's position and angle based on the keys being pressed
    # if keys[pygame.K_UP]:
    #     car_speed += 0.1
    #
    # if keys[pygame.K_DOWN]:
    #     car_speed -= 0.1
    #
    # if car_speed > 0:
    #     if keys[pygame.K_LEFT]:
    #         car_angle += 1
    #     if keys[pygame.K_RIGHT]:
    #         car_angle -= 1
    # elif car_speed < 0:
    #     if keys[pygame.K_LEFT]:
    #         car_angle -= 1
    #     if keys[pygame.K_RIGHT]:
    #         car_angle += 1
    MAX_SPEED = 5
    MIN_SPEED = -5
    ACCELERATION = 0.1
    TURN_SPEED = 1

    if keys[pygame.K_UP]:
        car_speed = min(car_speed + ACCELERATION, MAX_SPEED)

    if keys[pygame.K_DOWN]:
        car_speed = max(car_speed - ACCELERATION, MIN_SPEED)

    if keys[pygame.K_LEFT]:
        car_angle += TURN_SPEED * car_speed / MAX_SPEED
    elif keys[pygame.K_RIGHT]:
        car_angle -= TURN_SPEED * car_speed / MAX_SPEED

    car_speed = max(min(car_speed, MAX_SPEED), MIN_SPEED)
    # Update the car's position and angle based on its speed and angle
    car_x += math.cos(math.radians(car_angle)) * car_speed
    car_y -= math.sin(math.radians(car_angle)) * car_speed

    # Draw the road and car
    # screen.fill((0, 255, 0))
    screen.blit(track_img, (0, 0))
    rotated_car_img = pygame.transform.rotate(car_img, car_angle)
    car_rect = rotated_car_img.get_rect(center=(car_x, car_y))
    screen.blit(rotated_car_img, car_rect)

    # Update the screen
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)
