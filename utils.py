import pygame


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate(screen, image, pos_xy, angle):
    rotated_car_img = pygame.transform.rotate(image, angle)
    car_rect = rotated_car_img.get_rect(center=pos_xy)
    screen.blit(rotated_car_img, car_rect)
