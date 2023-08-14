# TODO: Enviar tarea a eduardo.laruta+tareas@gmail.com, enviar un .zip
# Tarea de los estudiantes: 1. Infografía_1_cayllan
# Tarea de las rectas: 2. Infografía_2_cayllan



# FIXME: We need to correct this function in order to graphic lines in the eight octants
def get_line(x0, y0, x1, y1):
    if abs(x1 - x0) > abs(y1 - y0):
        if x0 < x1:
            points = get_line_low(x0, y0, x1, y1)
        else:
            points = get_line_low(x1, y1, x0, y0)
    else:
        if y0 < y1:
            points = get_line_high(x0, y0, x1, y1)
        else:
            points = get_line_high(x1, y1, x0, y0)
    return points


def get_line_low(x0, y0, x1, y1):
    points = [(x0, y0)]
    d_x = x1 - x0
    d_y = y1 - y0
    # NOTE: Incremento de Y en las rectas con pendiente alta
    yi = 1
    if d_y < 0:
        yi = -1
        d_y = -d_y
    p_k = 2 * d_y - d_x
    x_k = x0
    y_k = y0
    # NOTE: La variable cambiante es Y
    while x_k < x1:
        if p_k > 0:
            y_k += yi
            p_k += 2 * d_y - 2 * d_x
        else:
            p_k += 2 * d_y
        x_k +=1
        points.append((x_k, y_k))
    return points


def get_line_high(x0, y0, x1, y1):
    points = [(x0, y0)]
    d_x = x1 - x0
    d_y = y1 - y0
    # NOTE: Incremento de X en las rectas con pendiente alta (Positiva o negativa)
    xi = 1
    if d_x < 0:
        xi = -1
        d_x = -d_x
    p_k = 2 * d_x - d_y
    x_k = x0
    y_k = y0
    # NOTE: La variable cambiante es X
    while y_k < y1:
        if p_k > 0:
            x_k += xi
            p_k += 2 * d_x - 2 * d_y
        else:
            p_k += 2 * d_x
        y_k +=1
        points.append((x_k, y_k))
    return points


# NOTE:
if __name__ == "__main__":
    print(get_line(5, 1, 1, 10))
