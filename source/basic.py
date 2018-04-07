import networkx as nx

def read_graph_from_file(filename, zero_based = False):
    G = nx.Graph()
    ofs = 1 if zero_based else 0;
    with open(filename) as f:
        for line in f:
            if line.startswith('p'):
                Node_number = int(line.rsplit(' ', 2)[1])
            if line.startswith('e'):
                a = list(map(int, line[2:].rstrip().split(' ')))
                G.add_edge(a[0]+ofs,a[1]+ofs)
    for x in range (1,Node_number):
        G.add_node(x)
    return G

G = read_graph_from_file("queen6_6.col")


def get_sample_1():
    G = nx.Graph()

    G.add_edge(1,2)

    G.add_edge(1,3)

    G.add_edge(2,4)
 
    G.add_edge(1,5)
 
    G.add_edge(2,6)
 
    G.add_edge(3,5)
 
    G.add_edge(4,3)

    G.add_edge(3,6)
 
    G.add_edge(1,4)

    G.add_edge(4,5)

    G.add_edge(4,6)
    G.add_edge(7,2)
 
    G.add_edge(8,3)

    G.add_edge(9,3)
 
    G.add_edge(9,4)

    return G




def get_sample_2():
    G = nx.Graph()

    G.add_edge(1,2)
    G.add_edge(1,5)
    G.add_edge(2,3)
    G.add_edge(1,6)
    G.add_edge(2,7)
    G.add_edge(3,4)
    G.add_edge(4,5)
    G.add_edge(3,8)
    G.add_edge(4,9)
    G.add_edge(5,10)
    G.add_edge(6,8)
    G.add_edge(6,9)
    G.add_edge(7,9)
    G.add_edge(7,10)
    G.add_edge(8,10)

    return G
#G = get_sample_2()