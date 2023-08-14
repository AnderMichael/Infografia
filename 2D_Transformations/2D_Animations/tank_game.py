# TODO: Agregar un nuevo tanque (jugador), matarse netre ellos ---- Tabris2015
import arcade
import random
from polygons_2d import Tank, Enemy

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Tank"
DEFAULT_FONT_SIZE = 20

SPEED = 10


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.rot_speed = 0.5
        self.speed = 10
        self.tank1 = Tank(
            200, 400, get_random_color(), arcade.color.RED, SCREEN_WIDTH, SCREEN_HEIGHT
        )
        self.ptank1 = 0
        self.tank2 = Tank(
            600, 400, get_random_color(), arcade.color.BLUE, SCREEN_WIDTH, SCREEN_HEIGHT
        )
        self.ptank2 = 0
        self.enemies = [
            Enemy(
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(0, SCREEN_HEIGHT - 60),
                random.randrange(10, 50),
            )
            for _ in range(10)
        ]

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.tank1.speed = SPEED
        elif symbol == arcade.key.S:
            self.tank1.speed = -SPEED
        elif symbol == arcade.key.A:
            self.tank1.angular_speed = 1.5
        elif symbol == arcade.key.D:
            self.tank1.angular_speed = -1.5
        elif symbol == arcade.key.E:
            self.tank1.shoot(20)

        if symbol == arcade.key.I:
            self.tank2.speed = SPEED
        elif symbol == arcade.key.K:
            self.tank2.speed = -SPEED
        elif symbol == arcade.key.J:
            self.tank2.angular_speed = 1.5
        elif symbol == arcade.key.L:
            self.tank2.angular_speed = -1.5
        elif symbol == arcade.key.U:
            self.tank2.shoot(20)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.W, arcade.key.S):
            self.tank1.speed = 0
        if symbol in (arcade.key.A, arcade.key.D):
            self.tank1.angular_speed = 0
        if symbol in (arcade.key.I, arcade.key.K):
            self.tank2.speed = 0
        if symbol in (arcade.key.J, arcade.key.L):
            self.tank2.angular_speed = 0

    def kill_enemies(self, tank: Tank):
        cont = 0
        for i, e in enumerate(self.enemies):
            e.detect_collision(tank)
            if not e.is_alive:
                self.enemies.pop(i)
                cont += 1
        return cont

    def on_update(self, delta_time: float):
        self.tank1.update(delta_time)
        self.tank1.detect_collision(self.tank2)
        self.ptank1 += self.kill_enemies(self.tank1)
        self.tank2.update(delta_time)
        self.tank2.detect_collision(self.tank1)
        self.ptank2 += self.kill_enemies(self.tank2)
        for e in self.enemies:
            e.detect_collision(self.tank2)
        if not self.tank1.is_alive or not self.tank2.is_alive:
            if self.tank1.is_alive:
                self.ptank1 += 1
            else:
                self.ptank2 += 1
            self.tank1 = Tank(
                200,
                400,
                get_random_color(),
                arcade.color.RED,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
            )
            self.tank2 = Tank(
                600,
                400,
                get_random_color(),
                arcade.color.BLUE,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
            )

    def on_draw(self):
        arcade.start_render()
        self.tank1.draw()
        self.tank2.draw()
        for e in self.enemies:
            e.draw()
        arcade.draw_text(
            "Jugador 1",
            10,
            SCREEN_HEIGHT - 30,
            arcade.color.RED,
            DEFAULT_FONT_SIZE,
        )
        arcade.draw_text(
            self.ptank1,
            210,
            SCREEN_HEIGHT - 30,
            arcade.color.RED,
            DEFAULT_FONT_SIZE,
        )
        arcade.draw_text(
            "Jugador 2",
            410,
            SCREEN_HEIGHT - 30,
            arcade.color.BLUE,
            DEFAULT_FONT_SIZE,
        )
        arcade.draw_text(
            self.ptank2,
            610,
            SCREEN_HEIGHT - 30,
            arcade.color.BLUE,
            DEFAULT_FONT_SIZE,
        )


if __name__ == "__main__":
    app = App()
    arcade.run()
