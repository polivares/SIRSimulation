import numpy as np
import matplotlib.pyplot as plt
import multinetx as mx
import Multilayer as ml

Net = ml.Network(100, 'erdos', {'rand': 0.5, 'seed': 200})
print(Net.getAdjMatrix().todense())