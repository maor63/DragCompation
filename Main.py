import csv
import itertools
from igraph import Graph




def main():
    train_csv = "train.csv"
    graph = load_csv(train_csv)
    assert (isinstance(graph, Graph))
    n = len(graph.vs)
    l = graph.similarity_jaccard()
    all_edges = list(itertools.combinations(xrange(n), 2))
    f = graph.get_eids(all_edges, error=False)
    non_edges = [all_edges[j] for j, e in enumerate(f) if e == -1]
    pass


def load_csv(train_csv):
    graph = Graph()
    f = open(train_csv, "r")
    csv_file = csv.DictReader(f)
    edges = set()
    nodes = set()
    for row in csv_file:
        v = int(row['node1'])
        u = int(row['node2'])
        nodes.add(v)
        nodes.add(u)
        edges.add((v, u))
    graph.add_vertices(len(nodes))
    graph.add_edges(edges)

    return graph

main()












