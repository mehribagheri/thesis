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

G = read_graph_from_file("myciel5.col")


# def get_sample_1():
#     G = nx.Graph()
#
#     d = []
#     v = []

'''
    Node_number = 9

    Matrix = np.zeros((Node_number,Node_number))

    G.add_edge(0,1)
    Matrix[0][1] = 1
    Matrix[1][0] = 1

    G.add_edge(0,2)
    Matrix[0][2] = 1
    Matrix[2][0] = 1

    G.add_edge(1,3)
    Matrix[1][3] = 1
    Matrix[3][1] = 1

    G.add_edge(0,4)
    Matrix[0][4] = 1
    Matrix[4][0] = 1

    G.add_edge(1,5)
    Matrix[1][5] = 1
    Matrix[5][1] = 1

    G.add_edge(2,4)
    Matrix[2][4] = 1
    Matrix[4][2] = 1




    G.add_edge(3,2)
    Matrix[3][2] = 1
    Matrix[2][3] = 1

    G.add_edge(2,5)
    Matrix[2][5] = 1
    Matrix[2][5] = 1

    G.add_edge(0,3)
    Matrix[0][3] = 1
    Matrix[3][0] = 1

    G.add_edge(3,4)
    Matrix[3][4] = 1
    Matrix[4][3] = 1

    G.add_edge(3,5)
    Matrix[3][5] = 1
    Matrix[5][3] = 1

    G.add_edge(6,1)
    Matrix[6][1] = 1
    Matrix[1][6] = 1

    G.add_edge(7,2)
    Matrix[7][2] = 1
    Matrix[2][7] = 1

    G.add_edge(8,2)
    Matrix[8][2] = 1
    Matrix[2][8] = 1

    G.add_edge(8,3)
    Matrix[8][3] = 1
    Matrix[3][8] = 1
    return G


def get_sample_2():
    G = nx.Graph()
    Node_number = 10

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
'''
