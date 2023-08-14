import arcade
import math

# Constante en Python siempre con mayúsculas
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Primeros Dibujos con Arcade"


def draw_florecita():
    ## Una florecita
    r = 40
    for ang in range(0, 361, 60):
        arcade.draw_circle_filled(
            300 + _compX(r, ang), 400 + _compY(r, ang), 30, arcade.color.YELLOW_ROSE
        )
    arcade.draw_circle_filled(300, 400, 50, arcade.color.AERO_BLUE)


def _compX(r, ang):
    return r * math.cos(math.radians(ang))


def _compY(r, ang):
    return r * math.sin(math.radians(ang))


def draw_fibonacci():
    r = [1, 1, 2, 3, 5, 8, 13, 21]
    for i in range(len(r)):
        # Quiero empezar viendo el problema horizontalmente
        arcade.draw_circle_filled(
            300 + _compY(100 + 20 * r[i], i * 60),
            400 + _compX(100 + 20 * r[i], i * 60),
            40,
            arcade.color.YELLOW_ROSE,
        )
    arcade.draw_circle_filled(300, 400, 40, arcade.color.AERO_BLUE)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Cambiar el color de fondo
    arcade.set_background_color(arcade.color.DARK_RED)

    # Iniciar render
    arcade.start_render()

    ### Modificar desde aquí

    # draw_florecita()
    # draw_fibonacci()

    ### Hasta aquí

    # Finalizar render
    arcade.finish_render()

    # Correr programa en el graficador
    arcade.run()


if __name__ == "__main__":
    main()
