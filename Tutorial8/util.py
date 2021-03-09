from joblib import Memory # for caching
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

os.makedirs('private', exist_ok=True)
memory = Memory(location="private",verbose=0)

@memory.cache
def plot_cluster_regions(X, Y, clusterer, target_names=None, ax=None, N=200):
    """Plot the cluster regions of a clusterer on a 2D dataset.
    
    Parameters
    ----------
    X (array-like): 2D input features.
    Y (array-like): 1D target values for X.
    clusterer (sklean): A clusterer trained to cluster X.
    target_names (array-like): array of possible target names. If None, infer from Y.
    ax (axis): axis to plot the boundaries.
    N: number of points for each dimension to scan for the decision boundaries.
    
    Return
    ------
    axis: axis for the plot of the decision boundaries
    """
    def color(target_array):
        return ((np.asarray(target_array).reshape(-1, 1) == target_names.reshape(1, -1)) *
                np.arange(len(target_names)).reshape(1, -1)).sum(axis=-1)
    
    if ax is None:
        ax = plt.gca()

    X_, Y_ = np.asarray(X), np.asarray(Y)

    X_min = X_.min(axis=0)
    X_max = X_.max(axis=0)
    x1, x2 = np.meshgrid(np.linspace(X_min[0], X_max[0], N),
                         np.linspace(X_min[1], X_max[1], N))

    if target_names is None:
        target_names = np.unique(Y_)

    c = color(Y_)
    yhat = clusterer.predict(np.c_[x1.ravel(), x2.ravel()]).reshape(x1.shape) 
    
    ax.contourf(x1, x2, yhat, alpha=0.4)
    scatter = ax.scatter(X_[:, 0], X_[:, 1], c=c, edgecolor='w', s=20)
    ax.set_xlim(X_min[0], X_max[0])
    ax.set_ylim(X_min[1], X_max[1])
    ax.add_artist(
        ax.legend(scatter.legend_elements()[0],
                  target_names,
                  loc="upper left",
                  title="Classes"))
    return ax
