import networkx as nx
import numpy as np
import modified_greedy_coloring
import time
import basic


from networkx.algorithms.approximation import min_weighted_vertex_cover
e =7

#def findsubsets(S,k):
#    return set(itertools.combinations(S, k))

G = basic.G

def cal_ranks(order):

    return dict([ (j, i + 1) for (i, j) in enumerate(order)])

def valid_colors(G, v, coloring, r):
    valid_colors = list(range(1, r + 1))
    for n in G[v]:
        if n < v and n in coloring:
            try:
                valid_colors.remove(coloring[n])
            except ValueError:
                pass
    return valid_colors


def exact_dsatur(G, clique, order, heu_coloring):

    # step 1
    w = len(clique)

    ranks = cal_ranks(order)

    r = max(heu_coloring.items(), key=lambda k: k[1])[1]
    if w == r:
        return heu_coloring
    l = w
    q = r
    best_coloring = heu_coloring


    U = dict()
    L = dict()

    coloring = dict()
    for v in G:
        U[v] = set(range(1, r + 1))

    n = len(G)

    coloring = dict()
    i = 1
    for v in clique:
        coloring[v] = i
        i += 1

    k = 1
    U = [[] for i in range(len(G) + 1)]
    L = [0] * (n + 1)

    counter = 0
    while True:
        counter += 1
        if counter == 100000:
            counter = 0


        U[k] = valid_colors(G, k, coloring, r)
        back = True
        goto_next = False
        while (True):
            if k in clique:
                if k == n:
                    goto_next = True

                else:
                    k += 1
                    break
            if not goto_next:

                if len(U[k]) == 0:
                    while True:
                        k -= 1
                        if k == 0 or not k in clique:
                            break
                    if k == 0:
                        return best_coloring
                    else:
                        if k <= 4:
                            pass
                        l = L[k]
                        continue

                next_color = min(U[k])
                coloring[k] = next_color
                U[k].remove(next_color)
                if next_color >= min(q, ranks[k]):
                    while True:
                        k -= 1
                        if k == 0 or not k in clique:
                            break
                    if k == 0:
                        return best_coloring
                    else:
                        if k <= 4:
                            pass
                        l = L[k]
                        continue

                if next_color > l:
                    l = next_color
            if goto_next or k == n:
                goto_next = False
                best_coloring = coloring.copy()
                q = l
                j = 1
                while coloring[j] != q:
                    j += 1
                k = j - 1
                l = q - 1


                continue
            else:
                L[k] = l
                k += 1

                break








def find_biggest_clique(G):
    max_cliques = np.array(list(nx.find_cliques(G)))
    mxn = max([len(c) for c in max_cliques])
    for i in max_cliques:
        if len(i) == mxn:
            return i


#d = []



start = time.clock()



#d = nx.coloring.greedy_color(G, strategy=nx.coloring.strategy_saturation_largest_first)
#print ("d= ",d)
#print(max(d.values())+1)
clique = find_biggest_clique(G)

d, order = modified_greedy_coloring.greedy_color(G, clique, strategy="DSATUR")


#nx.draw(G)

start_time = time.time()
coloring =  exact_dsatur(G, clique, order, d)
end_time = time.time()
print ("elapsed time for coloring before kernelization=", (end_time - start_time) * 1000)
print (coloring)
print  (max(coloring.items(), key=lambda k: k[1])[1])


print ( "G ", G.edges())




v_approx = min_weighted_vertex_cover(G)
print ("v_approx = " , len(v_approx))

vertex_cover = []

with open('output.out') as g:
    for line in g:
        vertex_cover.append(int(line))

print("vertex cover ", vertex_cover)
print("length =" ,len(vertex_cover))

#S = findsubsets(v,k)


outside_nodes_approx = set(G.nodes())-set(v_approx)

outside_nodes = set(G.nodes())-set(vertex_cover)

'''
for item in outside_nodes:
    for s in S :
        flag = False
        for y in s:
            if not G.has_edge(y,item):
              flag = True
        if not flag:
            X.append(item)
    if item not in X:
      G.remove_node(item)

'''



'''
for out_item in outside_nodes:
    for s in S:
        for index,item in enumerate(G.adjacency_list()):
            if set(s) <= set(item) :
                X.append(index+1)
       
    if out_item not in X:
        G.remove_node(out_item)
'''




'''
for out_item in outside_nodes:
    if len(adj_list[out_item-1]) >= k:
        counter = 0
        for i in adj_list[out_item-1]:
            if i in set(v):
                counter += 1
        if counter >= k:
            X.append(out_item)

for out_item in outside_nodes:
    if out_item not in X:
        G.remove_node(out_item)

'''
# print("node number of outside_nodes = " , len(outside_nodes))
# print("outside nodes = ", outside_nodes)
# print ("outside_approx ", outside_nodes_approx)
'''
def pick_random(s):
    if s:
        elem = s.pop()
        s.add(elem)
        return elem
'''


flag_list = []

X =[]


start_time = time.time()

for out_item in outside_nodes:
    if G[out_item] != []:

        if len(G[out_item]) == e and G[out_item] not in flag_list:

            X.append(out_item)
            flag_list.append(G[out_item])

for out_item in outside_nodes:
    if out_item not in X:
        G.remove_node(out_item)

end_time = time.time()
print ("elapsed time for kernelization =", (end_time - start_time) * 1000 )

print("resulted node number ", G.number_of_nodes())

G1 = nx.Graph()
G1 = nx.convert_node_labels_to_integers(G,1)

print ( "G1 ", G1.number_of_nodes())
print (G1.edges)
#map(lambda G.nodes: G.nodes, range(G.number_of_nodes()))
#y = []


#y = nx.coloring.greedy_color(G, strategy=nx.coloring.strategy_saturation_largest_first)

#print("y = ", y)
#print(max(y.values())+1)



clique = find_biggest_clique(G1)

d, order = modified_greedy_coloring.greedy_color(G1, clique, strategy="DSATUR")


#nx.draw(G)

start_time = time.time()
coloring =  exact_dsatur(G1, clique, order, d)
end_time = time.time()
print ("elapsed time for coloring after=", (end_time - start_time) * 1000 )
print (coloring)
print  (max(coloring.items(), key=lambda k: k[1])[1])
#nx.draw(max_clique)


# raw_input("Press Enter to continue...")





