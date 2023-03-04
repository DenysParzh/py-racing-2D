import pygame

from loader import track_surf, tire_track_img, track_img
import time

tire_tracks = []


def create_tire_track(center, angle, alpha):
    rotated_tire_track_img = pygame.transform.rotate(tire_track_img, angle)
    rotated_tire_track_img.set_alpha(alpha)
    tire_rect = rotated_tire_track_img.get_rect(center=center)
    track_surf.blit(rotated_tire_track_img, tire_rect)
    tire_tracks.append((time.time(), tire_rect, track_surf))


def remove_old_tire_tracks():
    now = time.time()
    i = 0
    while i < len(tire_tracks):
        track_time, track_rect, track_surf = tire_tracks[i]
        if now - track_time >= 5:
            bg_surf = track_img.subsurface(track_rect)
            track_surf.blit(bg_surf, track_rect)
            tire_tracks.pop(i)
        else:
            i += 1



def blit_rotate(screen, image, pos_xy, angle):
    rotated_car_img = pygame.transform.rotate(image, angle)
    car_rect = rotated_car_img.get_rect(center=pos_xy)
    remove_old_tire_tracks()
    screen.blit(track_surf, (0, 0))
    screen.blit(rotated_car_img, car_rect)