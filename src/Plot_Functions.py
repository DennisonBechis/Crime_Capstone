from matplotlib import pyplot as plt
import seaborn as sns

def Bar_plot(Ax, X_labels, Y_axis, x_name = False, y_name = False, color = 'blue'):

    X_ticks = [x for x in range(0,len(X_labels))]
    Ax.bar(X_ticks, Y_axis, color= color, align= 'center')
    Ax.set_xticks(ticks = X_ticks)
    Ax.set_xticklabels(X_labels)
    Ax.yaxis.grid(True)
    Ax.set_xlabel(x_name)
    Ax.set_ylabel(y_name)



def kde_plot(x, y, xlabel=False, ylabel=False, name = ''):

    ax = sns.set(style="ticks")
    ax = sns.jointplot(x, y, kind="kde", color='red', ylim=(-.5,12.5))
    ax.set_axis_labels(xlabel, ylabel, fontsize=18)
    plt.tight_layout()
    plt.savefig('../images/'+name+'.png')
    return ax
