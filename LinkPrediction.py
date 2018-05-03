import math
from igraph import Graph
import itertools


class LinkPrediction:
    @staticmethod
    def friend_measure(graph, v, u):
        v_neighbors = set(graph.neighbors(v))
        u_neighbors = set(graph.neighbors(u))
        assert (isinstance(graph, Graph))
        pairs = itertools.product(v_neighbors, u_neighbors)
        friend_measure = len(v_neighbors & u_neighbors)
        friend_measure += len([x for x in graph.get_eids(pairs, error=False) if x > -1])
        if friend_measure == 0:
            return 0
        return friend_measure / float(len(v_neighbors) * len(u_neighbors))

    @staticmethod
    def friend_measure_2(graph, v, u):
        v_neighbors = set(graph.neighbors(v))
        u_neighbors = set(graph.neighbors(u))
        v_neighbors2 = set()
        [v_neighbors2.update(graph.neighbors(n)) for n in v_neighbors]
        u_neighbors2 = set()
        [u_neighbors2.update(graph.neighbors(n)) for n in u_neighbors]
        edges = set(graph.get_edgelist())
        friend_measure = 0
        for v_neighbor in v_neighbors2:
            for u_neighbor in u_neighbors2:
                if v_neighbor != u_neighbor:
                    if (v_neighbor, u_neighbor) in edges or (u_neighbor, v_neighbor) in edges:
                        friend_measure += 1
                else:
                    friend_measure += 1
        return friend_measure / float(len(v_neighbors2) * len(u_neighbors2))

    @staticmethod
    def calculate_common_friends(graph, v, u):
        return len(set(graph.neighbors(v)).intersection(set(graph.neighbors(u))))

    @staticmethod
    def jacard_coefficient_2(graph, v, u):
        v_neighbors = set(graph.neighbors(v))
        u_neighbors = set(graph.neighbors(u))
        v_neighbors2 = set()
        [v_neighbors2.update(graph.neighbors(n)) for n in v_neighbors]
        u_neighbors2 = set()
        [u_neighbors2.update(graph.neighbors(n)) for n in u_neighbors]
        return float(len(v_neighbors2.intersection(u_neighbors2))) / float(len(v_neighbors2.union(u_neighbors2)))


def adamic_adar(graph, v, u):
    v_neighbors = set(graph.neighbors(v))
    u_neighbors = set(graph.neighbors(u))
    score = sum(
        list(map(lambda x: 1 / math.log(len(graph.neighbors(x)), 2), v_neighbors.intersection(u_neighbors))))
    return score


def friend_measure(graph, v, u):
    v_neighbors = set(graph.neighbors(v))
    u_neighbors = set(graph.neighbors(u))
    assert (isinstance(graph, Graph))
    pairs = itertools.product(v_neighbors, u_neighbors)
    friend_measure = len(v_neighbors & u_neighbors)
    friend_measure += len([x for x in graph.get_eids(pairs, error=False) if x > -1])
    if friend_measure == 0:
        return 0
    return friend_measure / float(len(v_neighbors) * len(u_neighbors))


def jacard_coefficient(graph, v, u):
    v_neighbors = set(graph.neighbors(v))
    u_neighbors = set(graph.neighbors(u))
    intersection = v_neighbors.intersection(u_neighbors)
    if len(intersection) == 0:
        return 0
    return float(len(intersection)) / float(len(v_neighbors.union(u_neighbors)))


def preferential_attachment(graph, v, u):
    return (graph.degree(v) * graph.degree(u)) / float((len(graph.vs) - 1) * (len(graph.vs) - 1))


def dice_similarity(graph, v, u):
    v_neighbors = set(graph.neighbors(v))
    u_neighbors = set(graph.neighbors(u))
    intersection = v_neighbors.intersection(u_neighbors)
    if len(intersection) == 0:
        return 0
    return 2 * float(len(intersection)) / float(len(v_neighbors) + len(u_neighbors))
