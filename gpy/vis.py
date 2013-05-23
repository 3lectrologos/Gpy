import numpy.matlib as np
import matplotlib.pyplot as plt


LIGHTGRAY = '#DDDDDD'
DARKGRAY = '#333333'
LIGHTBLUE = '#AAAADD'
DARKBLUE = '#6666BB'

def plot1(gp, ngrid=100, lim=None, k=range(-3, 4)):
    k = sorted(k)
    if lim is None:
        lim = (np.amin(gp.x[:, 1]), np.amax(gp.x[:, 1]))
    x = np.linspace(lim[0], lim[1], ngrid).T
    (m, v) = gp.inf(x)
    m = np.asarray(m).squeeze()
    v = np.asarray(v).squeeze()
    plt.plot(x, m,
             color=DARKBLUE,
             linewidth=2)
    for i in k:
        if i == 0: continue
        lo = m - i*np.sqrt(v)
        hi = m + i*np.sqrt(v)
        plt.fill_between(x, lo, hi,
                         linestyle='solid',
                         edgecolor=DARKGRAY,
                         facecolor=LIGHTGRAY,
                         alpha=0.2)
    plt.plot(gp.x, gp.y,
             'o',
             markersize=8,
             markeredgewidth=1,
             markeredgecolor=DARKGRAY,
             markerfacecolor=LIGHTBLUE)
    plt.xlim(lim)

def demo1():
    import gpy.core as gp
    import gpy.kernels as kernels
    hyp = {'mean': 0, 'cov': [-1, 1], 'lik': -1}
    k = kernels.SE(hyp)
    tmp = gp.GP(k, d=1)
    tmp.add([0.3, 0.5, 0.9], [1, 4, 0])
    plot1(tmp, lim=(0, 1))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
