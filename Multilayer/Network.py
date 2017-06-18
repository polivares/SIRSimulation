import multinetx as mx

class Network:
    def __init__(self,n=0, ntype = 'erdos', layer = 0, options={}):
        self._layer = layer
        self._n = n
        self._ntype = ntype
        if self._ntype == 'erdos':
            self._graph = mx.generators.erdos_renyi_graph(self._n, options["rand"], seed=options["seed"])
        self._adjacency_matrix = mx.adjacency_matrix(self._graph,weight="weight")

    def getAdjMatrix(self):
        return self._adjacency_matrix