from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from colorspacious import cspace_converter
from collections import OrderedDict


def bar_plot(ax, X_labels, Y_axis, x_name = False, y_name = False, color = 'blue'):

    X_ticks = [x for x in range(0,len(X_labels))]
    ax.bar(X_ticks, Y_axis, color= color, align= 'center')
    ax.set_xticks(ticks = X_ticks)
    ax.set_xticklabels(X_labels)
    ax.yaxis.grid(True)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    return ax

def kde_plot(x, y, xlabel=False, ylabel=False, name = ''):

    ax = sns.set(style="ticks")
    ax = sns.jointplot(x, y, kind="kde", color='red', ylim=(-.5,12.5))
    ax.set_axis_labels(xlabel, ylabel, fontsize=18)
    plt.tight_layout()
    plt.savefig('../images/'+name+'.png')
    return ax

def horizontal_bar(ax, labels, data, x_label = False, y_label = False, title = False):
    plt.style.use('classic')
    colors = ['tab:blue','tab:orange','tab:red','tab:green','tab:purple','tab:brown',
                    'tab:pink','tab:cyan','tab:olive','tab:blue','tab:grey','tab:brown']
    length_labels = np.arange(len(labels))
    ax.barh(length_labels, data, color=colors)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_yticks(length_labels)
    ax.set_yticklabels(labels)
    ax.set_title(title)
    plt.tight_layout()
    return ax

def line_plot(ax, x, y):
    ax.plot(x,y)
    return ax
