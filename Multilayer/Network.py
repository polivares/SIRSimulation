import multinetx as mx

class Network:
    def __init__(self,N=0,NType = 'erdos',randomizer = 0.5, seed = 200):
        self._N = N
        self._NType = NType
        if self._NType == 'erdos':
            self._graph = mx.generators.erdos_renyi_graph(self._N, randomizer, seed=seed)