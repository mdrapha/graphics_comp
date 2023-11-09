import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def sutherland_hodgman(subject_polygon, clip_polygon):
    output_polygon = subject_polygon.copy()

    # Itera sobre cada lado do clip_polygon
    for edge in range(4):
        clip_edge = clip_polygon[edge], clip_polygon[(edge + 1) % 4]

        # Inicializa a lista de vértices do polígono de saída
        input_polygon = output_polygon.copy()
        output_polygon = []

        # Itera sobre cada lado do polígono de entrada
        for i in range(len(input_polygon)):
            current_point = input_polygon[i]
            next_point = input_polygon[(i + 1) % len(input_polygon)]

            # Verifica se o ponto está dentro do clip_edge
            if inside(current_point, clip_edge):
                # Adiciona o ponto de interseção se necessário
                if not inside(next_point, clip_edge):
                    intersection = compute_intersection(current_point, next_point, clip_edge)
                    output_polygon.append(intersection)
                output_polygon.append(next_point)
            elif inside(next_point, clip_edge):
                # Adiciona o ponto de interseção se necessário
                intersection = compute_intersection(current_point, next_point, clip_edge)
                output_polygon.append(intersection)

    return output_polygon

def inside(point, edge):
    return (edge[1][0] - edge[0][0]) * (point[1] - edge[0][1]) > (edge[1][1] - edge[0][1]) * (point[0] - edge[0][0])

def compute_intersection(current_point, next_point, edge):
    x1, y1 = current_point
    x2, y2 = next_point
    x3, y3 = edge[0]
    x4, y4 = edge[1]

    # Calcula a interseção usando a equação da reta
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
        (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    )
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
        (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    )

    return x, y

# Função para desenhar o polígono
def draw_polygon(ax, polygon, color):
    polygon_patch = Polygon(polygon, closed=True, edgecolor=color, facecolor="none")
    ax.add_patch(polygon_patch)

# Função principal
def main():
    fig, ax = plt.subplots()

    # Leitura de vértices do polígono
    subject_polygon = []
    plt.title("Clique com o botão esquerdo para adicionar vértices e botão direito para finalizar")

    def onclick(event):
        if event.button == 1:  # Botão esquerdo
            subject_polygon.append((event.xdata, event.ydata))
            draw_polygon(ax, subject_polygon, "blue")
            plt.draw()
        elif event.button == 3:  # Botão direito
            clip_polygon = [(0, 0), (10, 0), (10, 10), (0, 10)]  # Quadro de recorte
            clipped_polygon = sutherland_hodgman(subject_polygon, clip_polygon)
            draw_polygon(ax, clipped_polygon, "red")
            plt.draw()

    cid = fig.canvas.mpl_connect("button_press_event", onclick)

    plt.show()

if __name__ == "__main__":
    main()
