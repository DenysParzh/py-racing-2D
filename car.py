import math

from loader import CAR_IMG
from screen_update import create_tire_track, blit_rotate


class AbstractCar:
    def __init__(self, max_vel, r_max_vel, rotation_vel):
        self.img = self.IMG
        self.x, self.y = self.START_POS
        self.rotation_vel = rotation_vel
        self.max_vel = max_vel
        self.min_vel = r_max_vel
        self.vel = 0
        self.angle = 0
        self.acceleration = 0.1
        self.acceleration_back = 0.05

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel * self.vel / self.max_vel
        elif right:
            self.angle -= self.rotation_vel * self.vel / self.max_vel

        if self.vel == self.max_vel:
            create_tire_track((self.x, self.y), self.angle, 200)

    def draw(self, screen):
        blit_rotate(screen, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration_back, self.min_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        self.x += math.cos(radians) * self.vel
        self.y -= math.sin(radians) * self.vel


class Car(AbstractCar):
    IMG = CAR_IMG
    START_POS = (100, 100)
    FRICTION = 0.05

    def reduce_speed(self):
        if self.vel > 0:
            self.vel -= self.FRICTION
        elif self.vel < 0:
            self.vel += self.FRICTION
        if math.fabs(self.vel) < self.FRICTION:
            self.vel = 0
        self.move()
