import arcade
import numpy as np

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Circulos con bresenham"


class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.vertices = [(100, 100), (50, 50), (50, 100), (100, 50)]
        self.pixel_size = 5
        self.thita = 0
        self.delta = 0
        self.circle_color = arcade.color.RED_DEVIL
        self.speed = 5
        self.velocity = [self.speed, self.speed]

    def on_update(self, delta_time: float):
        # self.xc += delta_time * self.velocity[0]
        # self.yc += delta_time * self.velocity[1]

        # Logica del rebote en X
        # if self.xc + self.r > SCREEN_WIDTH // self.pixel_size or self.xc - self.r < 0:
        #     self.velocity[0] = -1 * self.velocity[0]

        # Logica del rebote en Y
        # if self.yc + self.r > SCREEN_HEIGHT // self.pixel_size or self.yc - self.r < 0:
        #     self.velocity[1] = -1 * self.velocity[1]
        self.thita += delta_time * self.velocity[1]

        if self.thita == 360:
            self.thita = 0

        self.delta += self.velocity[1]
        if self.delta > SCREEN_HEIGHT - 200 or self.delta < 0:
            self.velocity[1] = -1 * self.velocity[1]

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        self.draw_scaled_polygon()

    def draw_grid(self):
        # lineas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2,
                0,
                v_l + self.pixel_size / 2,
                SCREEN_HEIGHT,
                [20, 20, 20],
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0,
                h_l + self.pixel_size / 2,
                SCREEN_WIDTH,
                h_l + self.pixel_size / 2,
                [20, 20, 20],
            )

    def draw_scaled_polygon(self):
        arcade.draw_polygon_outline(
            self.static_scale(
                self.thita,
                self.thita,
                self.translate(
                    self.delta,
                    self.delta,
                    self.static_rotation(self.thita, self.vertices),
                ),
            ),
            arcade.color.YELLOW,
        )

    def get_center(self, vertices):
        return np.mean(np.array(vertices), axis=0)

    def static_rotation(self, thita, vertices):
        xc, yc = self.get_center(vertices)
        Mt1 = np.array([[1, 0, -xc], [0, 1, -yc], [0, 0, 1]])
        Mr = np.array(
            [
                [np.cos(thita), -np.sin(thita), 0],
                [np.sin(thita), np.cos(thita), 0],
                [0, 0, 1],
            ]
        )
        Mt2 = np.array([[1, 0, xc], [0, 1, yc], [0, 0, 1]])
        Mt = np.dot(Mt2, np.dot(Mr, Mt1))
        return self.matrix_multiplication_transform(vertices, Mt)

    def static_scale(self, sx, sy, vertices):
        xc, yc = self.get_center(vertices)
        Mt1 = np.array([[1, 0, -xc], [0, 1, -yc], [0, 0, 1]])
        Ms = np.array(
            [
                [sx, 0, 0],
                [0, sy, 0],
                [0, 0, 1],
            ]
        )
        Mt2 = np.array([[1, 0, xc], [0, 1, yc], [0, 0, 1]])
        Mt = np.dot(Mt2, np.dot(Ms, Mt1))
        return self.matrix_multiplication_transform(vertices, Mt)

    def matrix_multiplication_transform(self, vertices, TM):
        v_array = np.array([[v[0], v[1], 1] for v in vertices])
        v_array = np.transpose(v_array)
        new_vertices_array = np.dot(TM, v_array)
        new_vertices = np.transpose(new_vertices_array[0:2, :])
        new_vertices = new_vertices.tolist()
        return new_vertices

    def translate(self, dx, dy, vertices):
        TM = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
        return self.matrix_multiplication_transform(vertices, TM)


if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()
