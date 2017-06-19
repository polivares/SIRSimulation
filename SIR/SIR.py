from scipy.integrate import odeint
import Multilayer as ml

def pend(y, t, network):
    print network.getAdjMatrix()
    for i in range(0,network.getNNodes()):


pend(1,1,ml.Network(100, 0, 'erdos', options))