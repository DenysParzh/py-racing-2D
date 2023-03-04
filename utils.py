import pygame


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


track_img = pygame.image.load('assets/images/track.png')
tire_track_img = scale_image(pygame.image.load('assets/images/car-tire.png'), 0.4)

# Set up the window
screen_width = track_img.get_width()
screen_height = track_img.get_height()

track_surf = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
track_surf.fill((0, 0, 0, 0))


def create_tire_track(center, angle, alpha):
    rotated_tire_track_img = pygame.transform.rotate(tire_track_img, angle)
    rotated_tire_track_img.set_alpha(alpha)
    tire_rect = rotated_tire_track_img.get_rect(center=center)
    track_surf.blit(rotated_tire_track_img, tire_rect)


def blit_rotate(screen, image, pos_xy, angle):
    rotated_car_img = pygame.transform.rotate(image, angle)
    car_rect = rotated_car_img.get_rect(center=pos_xy)
    screen.blit(track_surf, (0, 0))
    screen.blit(rotated_car_img, car_rect)
