# To find the Maximum Independent set (MIS)

def graphSets(graph):  # To define Sets of the graph
    if len(graph) == 0:  # The graph has no vertex
        return []
    if len(graph) == 1:  # The graph has 1 vertex
        return [list(graph.keys())[0]]
    vCurrent = list(graph.keys())[0]  # To select a current vertex (CV) from the graph

    graph2 = dict(graph)  # To create dictionary. To use Removing method
    del graph2[vCurrent]  # To delete a CV from the graph

    res1 = graphSets(graph2)  # Recursive call (RC) receives a maximal set. RC assumes CV, that isn't selected

    for v in graph[vCurrent]:  # To use Considering method. The selected vertex as part of Maximal set
        if v in graph2:  # To delete neighbor from the current subgraph
            del graph2[v]

    res2 = [vCurrent] + graphSets(graph2)  # Sum of VC and res1

    if len(res1) > len(res2):  # To return the result that is bigger
        return res1
    return res2
    # The end of defination of Sets of the graph


V = 11  # The number of vertices

E = [(1, 2),  # The edges
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
graph = dict([])  # To create dictionary for the graph
# Graph[VertexNumber V] = list[Neighbors of Vertex V]

for i in range(len(E)):  # To find a number for MIS
    v1, v2 = E[i]

    if v1 not in graph:
        graph[v1] = []
    if v2 not in graph:
        graph[v2] = []

    graph[v1].append(v2)  # To append (add) a vertex to list
    graph[v2].append(v1)

maximalIndependentSet = graphSets(graph)  # RC finds all vertices in MIS
for i in maximalIndependentSet:  # To output the result
    print(i, end=" ")
