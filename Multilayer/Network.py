import multinetx as mx

class Network:
    def __init__(self,n=0, ntype = 'erdos',options={}):
        self._N = n
        self._NType = ntype
        if self._NType == 'erdos':
            self._graph = mx.generators.erdos_renyi_graph(self._N, options["rand"], seed=options["seed"])
        self._adjacency_matrix = mx.adjacency_matrix(self._graph,weight="weight")

    def getAdjMatrix(self):
        return self._adjacency_matrix