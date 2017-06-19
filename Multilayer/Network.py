import multinetx as mx
import Node as node

class Network:
    __nodes = []
    def __init__(self,n=0, layer = 0, ntype = 'erdos', options={}):
        self.__layer = layer
        self.__n = n
        self.__ntype = ntype
        if self.__ntype == 'erdos':
            self.__graph = mx.generators.erdos_renyi_graph(self.__n, options["rand"], seed=options["seed"])
        self.__adjacency_matrix = mx.adjacency_matrix(self.__graph,weight="weight")
        for i in range(0,self.__n):
            self.__nodes.append(node.Node(i, self.__layer))

    def getAdjMatrix(self):
        return self.__adjacency_matrix

    def getNNodes(self):
        return self.__n

    def getNodes(self):
        return self.__nodes