"""
Модуль алгоритмов нахождения независимого множества
"""


# To find the Maximum Independent set (MIS)
def graph_sets(graph) -> list:  # -> list type hints or annotation type  == def graph_sets(graph):
    """
    Рекурсивная функция, которая ищет max независ. множество
    :param graph:
    :return:
    """
    # два if это базовые случаи или терминальные случаи
    if not graph:  # len(graph) == 0  pep8
        return []  # значит нет vertex
    if len(graph) == 1:  # The graph has 1 vertex
        return list(graph.nodes)  # приведение к списку в явном виде, потому что не можем сложить python list + nx NodeView
    current_vertex = list(graph.nodes)[0]  # берется первая по индексу вершина из текущего графа

    graph2 = graph.copy()  # метод copy() в nx.Graph который полностью копирует граф
    graph2.remove_node(current_vertex)  # удаляем узел со связями этого узла. Это контролирует nx.Graph

    res1 = graph_sets(graph2)  # рекурсивный вызов для поиска независимого подмножество

    for neighbour in graph.neighbors(current_vertex):  # передираем соседей текущего узла graph.neighbors из nx.Graph
        if neighbour in graph2:  # содержатся ли сосед текущего узла в графе без текущего узла
            graph2.remove_node(neighbour)  # если есть удаляем соседа из копии графа

    res2 = [current_vertex] + graph_sets(graph2)  # конкатенация текущего узла с MIS графа откуда удален текущий узел и все соседи текущего узла

    return max(res1, res2, key=len)  # ключевая функция для поиска списка максимальной длины, а не поиска максимума по значениям
