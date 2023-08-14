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
        self.pixel_size = 5
        self.xc = 80
        self.yc = 20
        self.r = 20
        self.circle_color = arcade.color.RED_DEVIL

        self.speed = 25
        self.velocity = [self.speed, self.speed]

    def on_draw(self):
        arcade.start_render()
        vertices = [(100, 100), (50, 50), (50, 100), (100, 50)]
        arcade.draw_polygon_outline(vertices, arcade.color.YELLOW)
        arcade.draw_polygon_outline(
            self.static_scale(3,3, vertices), arcade.color.YELLOW
        )

    # Traslación lenta
    def translate(self, dx, dy, vertices):
        new_vertices = [(v[0] + dx, v[1] + dy) for v in vertices]
        return new_vertices

    # Traslación con una transformada lineal
    def translate2(self, dx, dy, vertices):
        TM = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
        return self.matrix_multiplication_transform(vertices, TM)

    def matrix_multiplication_transform(self, vertices, TM):
        v_array = np.array([[v[0], v[1], 1] for v in vertices])
        v_array = np.transpose(v_array)
        new_vertices_array = np.dot(TM, v_array)
        new_vertices = np.transpose(new_vertices_array[0:2, :])
        new_vertices = new_vertices.tolist()
        return new_vertices

    # Rotación lineal
    def rotation(self, thita, vertices):
        thita = np.radians(thita)
        TM = np.array(
            [
                [np.cos(thita), -np.sin(thita), 0],
                [np.sin(thita), np.cos(thita), 0],
                [0, 0, 1],
            ]
        )
        return self.matrix_multiplication_transform(vertices, TM)

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

    def get_center(self, vertices):
        return np.mean(np.array(vertices), axis=0)


if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()
