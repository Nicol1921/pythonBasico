# Definir el tablero de ajedrez (8x8)
tablero = [[0] * 8 for _ in range(8)]

# Definir movimientos de las piezas
movimientos_piezas = {
    'peon_blanco': [(1, 0)],
    'peon_negro': [(-1, 0)],
    'torre': [(1, 0), (-1, 0), (0, 1), (0, -1)],
    'caballo': [(1, 2), (1, -2), (-1, 2), (-1, -2),
                (2, 1), (2, -1), (-2, 1), (-2, -1)],
    'alfil': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
    'reina': [(1, 0), (-1, 0), (0, 1), (0, -1),
              (1, 1), (1, -1), (-1, 1), (-1, -1)],
    'rey': [(1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)]
}


def generar_posiciones(posicion, movimientos, num_movimientos):
    if num_movimientos == 0:
        return [posicion]

    posiciones = []
    for movimiento in movimientos:
        dx, dy = movimiento
        x, y = posicion
        nueva_posicion = (x + dx, y + dy)

        if 0 <= nueva_posicion[0] < 8 and 0 <= nueva_posicion[1] < 8:
            posiciones.extend(generar_posiciones(nueva_posicion, movimientos, num_movimientos - 1))

    return posiciones


def obtener_posiciones_iniciales():
    posiciones_iniciales = []
    for i in range(8):
        for j in range(8):
            posiciones_iniciales.append((i, j))
    return posiciones_iniciales


def contar_posiciones(n):
    posiciones_iniciales = obtener_posiciones_iniciales()
    posiciones_finales = []

    for posicion in posiciones_iniciales:
        posiciones_finales.extend(generar_posiciones(posicion, movimientos_piezas['peon_blanco'], n))
        posiciones_finales.extend(generar_posiciones(posicion, movimientos_piezas['peon_negro'], n))

    return len(set(posiciones_finales))


# Ejemplo de uso
n_movimientos = 3
resultado = contar_posiciones(n_movimientos)
print(f"Se puede llegar a {resultado} posiciones diferentes después de {n_movimientos} movimientos válidos.")
