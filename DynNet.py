import networkx as nx
import random 

# Graph Declaration (undirected sample graph with 10 vertices)--------------

g = nx.Graph()

g.add_nodes_from(range(10))                        
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,6)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(3,6)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(5,7)
g.add_edge(5,9)
g.add_edge(6,7)
g.add_edge(6,8)
g.add_edge(7,8)
g.add_edge(7,9)
g.add_edge(8,9)


for e in g.edges() :        # list containing edge weight values over time 
    g[e[0]][e[1]]['Weight'] = [random.randint(2,5) for i in range(100)]






# Modified Dijkstra's -----------

def mod_dijk(g,s):

    d={}
    fin={}
    
    for i in range(g.number_of_nodes()):
        d[i]=100000000000
        fin[i]=100000000000
        
    d[s]=0
    fin[s]=0
    
    while len(d):

        u = min(d,key=d.get)
        

        for i in g[u].keys():

            if i in d.keys() and fin[i] > fin[u] + g[u][i]['Weight'][fin[u]]:
                d[i] = d[u] + g[u][i]['Weight'][d[u]]
                fin[i] = d[i]

        d.pop(u)
        
    return fin

            
# Sample queries ---------------------

q=[]


for _ in range(100):
    q.append((random.randint(0,9),random.randint(0,9)))
    
#  Path and Edge ---------------------




def path_multi_query(g,queries):                                # takes queries in list format [(s1,d1), (s2,d2)......]

    paths=[]							# final list that will contain calculated paths for every query
1
    for q in queries:

        path=[]

        if q[0]==q[1]:
            paths.append(path)
            continue
        
        a,b = mod_dijk(g,q[0])					# sequentially routing every query 

        nex = q[1]
        sta = b[nex]
        path.append(nex)

        while True:						# changing the edge weight list after rounting a query.
            path.append(sta)
            temp = a[sta]
            while temp <  a[nex]:
                g[sta][nex]['Weight'][temp]+=1
                temp+=1

            if sta ==q[0]:
                break
            temp = sta
            sta = b[sta]
            nex = temp

        paths.append(path)
    return paths
