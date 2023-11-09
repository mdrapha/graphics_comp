def cohen_sutherland(xmin, ymin, xmax, ymax, x1, y1, x2, y2):
    # Calcula os códigos de região para os pontos inicial e final da linha
    code1 = calculate_region_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = calculate_region_code(x2, y2, xmin, ymin, xmax, ymax)

    while True:
        # Se ambos os códigos são 0, a linha está completamente dentro da janela
        if code1 == 0 and code2 == 0:
            draw_line(x1, y1, x2, y2)
            break
        # Se a interseção das regiões é não-nula, a linha está completamente fora
        elif code1 & code2 != 0:
            break
        else:
            # Escolhe um ponto externo
            code = code1 if code1 != 0 else code2

            # Calcula as coordenadas de interseção
            if code & 8:
                x_int = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y_int = ymax
            elif code & 4:
                x_int = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y_int = ymin
            elif code & 2:
                y_int = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x_int = xmax
            elif code & 1:
                y_int = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x_int = xmin

            # Atualiza as coordenadas do ponto externo
            if code == code1:
                x1, y1 = x_int, y_int
                code1 = calculate_region_code(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x_int, y_int
                code2 = calculate_region_code(x2, y2, xmin, ymin, xmax, ymax)

    # Fim da função

# Função auxiliar para calcular o código de região
def calculate_region_code(x, y, xmin, ymin, xmax, ymax):
    code = 0
    if x < xmin:
        code |= 1
    elif x > xmax:
        code |= 2
    if y < ymin:
        code |= 4
    elif y > ymax:
        code |= 8
    return code

# Função para desenhar a linha
def draw_line(x1, y1, x2, y2):
    # Coloque aqui a lógica para desenhar a linha
    pass

# Exemplo de uso
cohen_sutherland(0, 0, 10, 10, 2, 3, 8, 9)
