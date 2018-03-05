import networkx as nx

import basic

G = basic.G


# def bronk2(R, P, X, g, seen = None):
#     if P == [] and X == []:
#         yield R
#     else:
#         pivot = random.choice(P + X)
#         Q = set(P) - set(adj_list[pivot ])
#         if seen == None:
#            seen = set()
#         for v in Q:
#             if v not in seen:
#                  R_v = R + [v]
#                  P_v = [v1 for v1 in P if v1 in adj_list[v]]
#                  X_v = [v1 for v1 in X if v1 in adj_list[v]]
#                  seen.add(v)
#                  for r in bronk2(R_v, P_v, X_v, g, seen):
#                     yield r
#                  seen.remove(v)
#                  P.remove(v)
#                  X.append(v)
#

Q2 = list(nx.find_cliques(G))

#list(bronk2([], range(G.number_of_nodes()), [], Matrix))
max_clique = max([len(i) for i in Q2])

print ("maxxx =", max_clique)

#print "4444",  len([i for i in Q2 if len(i) == 4])

print ("Q2= ",Q2)








file = open('ver.dat', 'w')
file.write('set Q := ' )
file.write('\n')

for i in range(0,len(Q2)):
    file.write('(' + str(i) + ' , *) ')
    for j in range(0, len(Q2[i])):
        file.write(str(Q2[i].__getitem__(j)))
        if j != len(Q2[i])-1:
          file.write(' , ')

    file.write('\n')

file.write(';')
file.write('\n')

cnt = set()
Idx =()

for i in range(0, len(Q2)):
    Idx = Idx + (i,)
    cnt.add((i,len(Q2[i])))





file.write('set V := ' + ','.join(str(v) for v in G.nodes())+';')
file.write('\n')
file.write('set E := ' + ','.join(str(e) for e in G.edges())+';')
file.write('\n')
file.write('set Idx := ' + ','.join(str(i) for i in Idx)+';')
file.write('\n')
#file.write('set Q := ' + ','.join(str(q) for q in Q2)+';')
file.write('set cnt := ' + ','.join(str(i) for i in cnt)+';')
file.close()