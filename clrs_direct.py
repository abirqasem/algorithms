"""

TODO: Please Ignore this for immediate idiom work. This is needed if want to expand the algorithm training idea
or improve on the App at a later date
1. Graph init should be able to do bidirectional
2. Coloring and tracing if we make it algorithm

"""

import sys

class Graph:
    """ Reprsents a graph as an adjacency list and some of its properties and functions to support graph coloring  """
    VERTEX_PROPS = {} # key is vertex label and values are color etc.


    def __init__ (self, data_source):
        g = {}

        #TODO: Ignore for idiom work we may to make it generic for any data source for now just text file
        f=open(data_source, "r")
        lines =f.readlines()
        for line in lines:
            # every  vertices read in
            if line[0] != "#":
                v0, v1 = line.split() # unpack them
                Graph.VERTEX_PROPS[v1]={"color":"", "d":"", "parent":""}
                Graph.VERTEX_PROPS[v0]={"color":"", "d":"", "parent":""}
                if v0 in g:
                    if not (v1 in g [v0]):
                        g[v0].append (v1)
                else:
                    g[v0] = [v1]
                if v1 in g:
                    if not (v0 in g [v1]):
                        g[v1].append (v0)
                else:
                    g[v1] = [v0]

        self.graph = g
        return

    def set_vertex_props (self, vertex, **props):

        if "color" in props:
            Graph.VERTEX_PROPS [vertex]["color"] = props["color"]
        if "parent" in props:
            Graph.VERTEX_PROPS [vertex]["parent"] = props["parent"]
        if "d" in props:
            Graph.VERTEX_PROPS [vertex]["d"] = props["d"]

    def get_vertex_props (self, vertex):

        if vertex in Graph.VERTEX_PROPS:
            return Graph.VERTEX_PROPS [vertex]
        else:
            return None

    def get_parent (self, vertex):

        if vertex in Graph.VERTEX_PROPS:
            return Graph.VERTEX_PROPS [vertex]["parent"]
        else:
            return None

    def show (self):
        print(self.graph)
        return

    def print_props (self):
        print (Graph.VERTEX_PROPS)
        return



########################### End Class Graph ###########################################



def BFS (G,s):
    for u in G.graph:
        G.set_vertex_props (u, color="WHITE", parent=None, d=sys.maxsize)
    G.set_vertex_props (s, color="GRAY", parent=None, d=0)

    Q = []
    Q.append(s)


    while len(Q) !=0:
        u= Q.pop(0)
        for v in G.graph[u]:
            if G.get_vertex_props (v)["color"]=="WHITE":
                G.set_vertex_props (v, color="GRAY", parent=u, d=G.get_vertex_props (u)["d"]+1)
                Q.append(v)
        G.set_vertex_props (u, color="BLACK")


    return G

def print_path (G, s, v):
    if v==s:
        print (" --> " + s, end='')
    elif G.get_parent(v) == None:
        print ("No path")
    else:
        print_path (G, s, G.get_parent(v))
        print (" --> " + v, end='')
    return



def main ():
    G= Graph (sys.argv[1])
    BFS (G,sys.argv[2])
    print_path (G, sys.argv[2], sys.argv[3])
    print ("\n")




if __name__ == '__main__':
    main()
