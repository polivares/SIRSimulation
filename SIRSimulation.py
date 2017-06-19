import numpy as np
import matplotlib.pyplot as plt
import multinetx as mx
import nepidemix as nep
import Multilayer as ml

from scipy.integrate import odeint

options = {'rand': 0.5, 'seed': 200}
Net = ml.Network(3, 0, 'erdos', options)
print(Net.getNodes()[0])

