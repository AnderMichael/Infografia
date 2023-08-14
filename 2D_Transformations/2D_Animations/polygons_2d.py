import numpy as np
import arcade
import math


class Polygon2D:
    def __init__(self, vertices, color, rot_speed=0):
        self.vertices = vertices
        self.color = color
        self.div = 1 if rot_speed == 0 else rot_speed

    def translate(self, dx, dy):
        TM = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

        return self.apply_transform(TM)

    def rotate(self, theta, pivot=None):
        xc, yc = pivot if pivot is not None else self.get_center()
        theta = theta * self.div
        Mt1 = np.array([[1, 0, -xc], [0, 1, -yc], [0, 0, 1]])
        Mr = np.array(
            [
                [np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0],
                [0, 0, 1],
            ]
        )
        Mt2 = np.array([[1, 0, xc], [0, 1, yc], [0, 0, 1]])

        TM = np.dot(Mt2, np.dot(Mr, Mt1))

        return self.apply_transform(TM)

    def scale(self, sx, sy, pivot=None):
        xc, yc = pivot if pivot is not None else self.get_center()
        Mt1 = np.array([[1, 0, -xc], [0, 1, -yc], [0, 0, 1]])
        Ms = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
        Mt2 = np.array([[1, 0, xc], [0, 1, yc], [0, 0, 1]])

        TM = np.dot(Mt2, np.dot(Ms, Mt1))

        return self.apply_transform(TM)

    def apply_transform(self, tr_matrix):
        v_array = np.transpose(np.array([[v[0], v[1], 1] for v in self.vertices]))
        self.vertices = np.transpose(np.dot(tr_matrix, v_array)[0:2, :]).tolist()

    def get_center(self):
        return np.mean(np.array(self.vertices), axis=0)

    def draw(self):
        arcade.draw_polygon_outline(self.vertices, self.color, 5)


class Tank:
    def __init__(self, x, y, colorWheels, colorBody, screen_width=0, screen_height=0) -> None:
        self.x = x
        self.y = y
        self.speed = 0
        self.angular_speed = 0
        self.theta = math.radians(90)
        self.is_alive = True
        self.body = Polygon2D(
            [(x - 50, y), (x, y + 100), (x + 50, y)], colorBody
        )
        self.wheels = [
            Polygon2D(
                [
                    (x - 50, y),
                    (x - 50, y + 50),
                    (x - 25, y),
                    (x - 25, y + 50),
                ],
                colorWheels,
            ),
            Polygon2D(
                [
                    (x + 50, y),
                    (x + 50, y + 50),
                    (x + 25, y),
                    (x + 25, y + 50),
                ],
                colorWheels,
            ),
        ]
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.bullets = []

    def shoot(self, bullet_speed):
        self.bullets.append((self.x, self.y, self.theta, bullet_speed))

    def update(self, delta_time: float):
        dtheta = self.angular_speed * delta_time
        dx = self.speed * math.cos(self.theta)
        dy = self.speed * math.sin(self.theta)
        if self.check_boundaries(self.x + dx, self.y + dy):
            self.theta += dtheta
            self.x += dx
            self.y += dy
            self.body.translate(dx, dy)
            self.wheels[0].translate(dx, dy)
            self.wheels[1].translate(dx, dy)
        self.body.rotate(dtheta, pivot=(self.x, self.y))
        self.wheels[0].rotate(dtheta, pivot=(self.x, self.y))
        self.wheels[1].rotate(dtheta, pivot=(self.x, self.y))
        self.update_bullets(delta_time)

    def update_bullets(self, delta_time):
        for i, (x, y, theta, speed) in enumerate(self.bullets):
            new_x = x + speed * math.cos(theta)
            new_y = y + speed * math.sin(theta)
            if self.check_boundaries(new_x, new_y):
                self.bullets[i] = (new_x, new_y, theta, speed)
            else:
                self.bullets.pop(i)

    def check_boundaries(self, new_x, new_y):
        check = (
            new_x <= self.SCREEN_WIDTH
            and new_x > 0
            and new_y <= self.SCREEN_HEIGHT - 50
            and new_y > 0
        )
        return check

    def draw(self):
        if self.is_alive:
            self.body.draw()
            self.wheels[0].draw()
            self.wheels[1].draw()
            arcade.draw_point(self.x, self.y, arcade.color.RED, 4)

            for bx, by, theta, speed in self.bullets:
                arcade.draw_point(bx, by, arcade.color.YELLOW, 3)
        else:
            arcade.finish_render()

    def detect_collision(self, tank):
        for bullet in tank.bullets:
            if self.distance_to(bullet) < 50:
                self.is_alive = False

    def distance_to(self, bullet):
        xb, yb, tb, sb = bullet
        return math.sqrt((xb - self.x) ** 2 + (yb - self.y) ** 2)

class Enemy:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.is_alive = True
    
    def detect_collision(self, tank: Tank):
        for bullet in tank.bullets:
            if self.distance_to(bullet) < self.r:
                self.is_alive = False
    
    def distance_to(self, bullet):
        xb, yb, tb, sb = bullet
        return math.sqrt((xb - self.x)**2 + (yb - self.y)**2)

    def draw(self):
        if self.is_alive:
            arcade.draw_circle_filled(self.x, self.y, self.r, arcade.color.RED_DEVIL)