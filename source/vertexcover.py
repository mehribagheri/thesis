"find the maximal cliques and write the data needed for AMPL to the file"


import networkx as nx

import basic



G = basic.G


"find cliques on the graph"
Q2 = list(nx.find_cliques(G))


max_clique = max([len(i) for i in Q2])

print ("length of the biggest clique =", max_clique)



print ("list of cliques = ",Q2)


"write  the data needed for AMPL on the file ver.dat "

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
file.write('set cnt := ' + ','.join(str(i) for i in cnt)+';')
file.close()