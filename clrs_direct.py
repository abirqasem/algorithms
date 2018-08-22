"""

TODO:

1. Graph init should be able to do bidirectional
2. discover function as opposed to  VERTEX_PROPS multiple lines
3. Graph should just print the adjacency list
4. Page 596 tracing should be used as a guideline to show BFS - not sure yet
5. Data structure to avoid or encapsulate the VERTEX_PROPS
6. Page 601 recursion and print_path fix it






"""

import sys, numpy

class Graph:
    """ Reprsents a graph as an adjacency set and some of its basic functions """

    def __init__ (self, data_source):
        g = {}
        #TODO: we may to make it generic for any data source for now just text file
        f=open(data_source, "r")
        lines =f.readlines()
        for line in lines:
            # every  vertices read in
            v0, v1 = line.split() # unpack them
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

    def show (self):
        print(self.graph)
        return


    def get_matrix (self):
        # there appears to be a bug
        adjlist = self.graph
        i =0
        index_map = {}
        for v in adjlist:
            index_map [v]=i
            i=i+1

        size = len(adjlist)
        mat = numpy.zeros ([size, size])

        for v0 in adjlist:
            for v1 in adjlist[v0]:
                print (v0, v1)
                #print (index_map[v0], index_map[v1])
                #mat [v0, v1] =1
        return (mat,index_map)










########################### End Class Graph ###########################################




VERTEX_PROPS = {} # key is vertex label and values are color etc.

def make_vertex_string (v):
    vs = v
    if (v in VERTEX_PROPS):
        try:
            color = VERTEX_PROPS[v]["color"]
            vs = vs + color
        except KeyError as e:
            pass

        try:
            d = VERTEX_PROPS[v]["d"]
            vs = vs + str(d)
            pass
        except KeyError as e:
            pass

        try:
            pie = VERTEX_PROPS[v]["pie"]
            vs = vs + (pie if pie != None else "")
        except KeyError as ke:
            pass

    return vs



def show_graph_props (G):
    graph_string = ""
    for v in G:
        graph_string = graph_string + make_vertex_string(v) + "--> "
        neigbours = G[v]
        for neigbour in neigbours:
            graph_string = graph_string + make_vertex_string(neigbour) + " "
        graph_string = graph_string + "\n"

    print (graph_string)


def init_graph_as_adjlist (datasource):

    g = {}

    f=open(datasource, "r")
    lines =f.readlines()
    for line in lines:
        # every  vertices read in
        v0, v1 = line.split() # unpack them
        VERTEX_PROPS[v1]={"color":"", "d":"", "pie":""}
        VERTEX_PROPS[v0]={"color":"", "d":"", "pie":""}

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
    return g


def BFS (G,s):
    for u in G:
        VERTEX_PROPS [u]["color"] = "WHITE"
        VERTEX_PROPS[u]["pie"] = None
        VERTEX_PROPS[u]["d"] = sys.maxsize

    VERTEX_PROPS[s]["color"] = "GRAY"
    VERTEX_PROPS[s]["pie"] = None
    VERTEX_PROPS[s]["d"] = 0

    Q = []
    Q.append(s)

    while len(Q) !=0:
        u= Q.pop(0)
        for v in G[u]:
            if VERTEX_PROPS[v]["color"] =="WHITE":
                VERTEX_PROPS[v]["color"] = "GRAY"
                VERTEX_PROPS[v]["pie"] = u
                VERTEX_PROPS[v]["d"] = VERTEX_PROPS[u]["d"] +1
                Q.append(v)
        VERTEX_PROPS[u]["color"] ="BLACK"

    return



def print_path (G, s, v):
    """ does not work """
    if v==s:
        print (s)
    elif VERTEX_PROPS[v]["pie"] == None:
        print (" No path")
    else:
        print_path (G, s, VERTEX_PROPS[v]["pie"])
        print (v)
    return







def main ():

    #G= init_graph_as_adjlist ("kormen1.txt")
    #print (G)


    G= Graph ("kormen0.txt")
    G.show()
    print(G.get_matrix())
    #show_graph_props (G)
    #print (make_vertex_string ("5"))
    #print(VERTEX_PROPS)
    #BFS (G,"1")
    #show_graph_props(G)
    #print (VERTEX_PROPS)
    #print_path (G, "1","10")
if __name__ == '__main__':
    main()
