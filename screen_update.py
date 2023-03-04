import pygame

from loader import track_surf, tire_track_img


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