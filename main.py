import networkx as nx
import matplotlib.pyplot as plt


# To find the Maximum Independent set (MIS)
def graph_sets(graph):  # To define Sets of the graph
    if len(graph) == 0:  # The graph has no vertex
        return []
    if len(graph) == 1:  # The graph has 1 vertex
        return list(graph.nodes)
    current_vertex = list(graph.nodes)[0]  # To select a current vertex (CV) from the graph

    graph2 = graph.copy()  # Copy graph. To use Removing method
    graph2.remove_node(current_vertex)  # To delete a CV from the graph

    res1 = graph_sets(graph2)  # Recursive call (RC) receives a maximal set. RC assumes CV, that isn't selected

    for neighbour in graph.neighbors(current_vertex):  # To use Considering method. The selected vertex as part of Maximal set
        if neighbour in graph2:  # To delete neighbor from the current subgraph
            graph2.remove_node(neighbour)

    res2 = [current_vertex] + graph_sets(graph2)  # Sum of VC and res1

    return max(res1, res2, key=len)  # To return the result that is bigger


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
    graph = nx.Graph()
    graph.add_edges_from(
        [(1, 2),  # The edges
         (1, 10),
         (1, 10),
         (1, 11),
         (2, 3),
         (2, 11),
         (3, 4),
         (3, 11),
         (4, 5),
         (4, 11),
         (5, 6),
         (5, 11),
         (6, 7),
         (6, 11),
         (7, 8),
         (7, 11),
         (8, 9),
         (8, 11),
         (9, 10),
         (1, 11)]
    )

    maximal_independent_set = graph_sets(graph)  # RC finds all vertices in MIS
    draw_graph(graph, maximal_independent_set)
    for i in maximal_independent_set:  # To output the result
        print(i, end=" ")
