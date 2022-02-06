import networkx as nx  # pip install networkx
import matplotlib.pyplot as plt

from mis_solver import graph_sets


def main():
    filename = "src_graph.txt"
    list_edges = get_list_edges(filename)

    graph_from_file = nx.Graph()
    graph_from_file.add_edges_from(list_edges)
    mis = graph_sets(graph_from_file)

    draw_graph(graph_from_file, mis)

    print(f"Размер mis = {len(mis)}")
    print(f"Содержимое mis = {mis}")


def get_list_edges(filename):
    """
    Считали граф из файла

    :param filename: файл с edges
    :return: Список списков, где вложенный список это пара узлов
    """
    with open(filename) as file:
        list_edges = []
        for line in file:
            line = line.rstrip()
            split_values = line.split()
            list_edges.append(split_values)

        return list_edges


def draw_graph(graph, max_independent_set):
    node_color = [
        "red" if node in max_independent_set else "blue"
        for node in graph
    ]
    nx.draw(
        graph,
        with_labels=True,
        font_weight="bold",
        node_color=node_color,
    )
    plt.show()


if __name__ == '__main__':
    main()
