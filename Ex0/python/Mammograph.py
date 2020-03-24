import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])

mylink = '../datasets/mammographic_masses.data'

df     = pd.read_table(mylink,header=None, delimiter=",")

df     = df.replace('?', np.nan)

data   = df.to_numpy().astype("float64")

# Attributes
#    - BI-RADS assessment:    2
#    - Age:                   5
#    - Shape:                31
#    - Margin:               48
#    - Density:              76
#    - Severity:              0

fig,ax =  plt.subplots(3,2,figsize=(13,8), sharex=False, sharey=False)
fig.subplots_adjust(hspace=0.5, wspace=0.3)


my_data = data[:,0]
my_data[np.isnan(my_data)] = -1
labels, counts = np.unique(my_data, return_counts=True)
ax[0][0].grid(alpha=0.2)
ax[0][0].bar(labels[1:-1], counts[1:-1], align='center',edgecolor="black")
ax[0][0].set_xticks(labels[1:-1])
ax[0][0].set_title("BI-RADS (ordinal)")
ax[0][0].set_ylabel("age [Years]")
ax[0][0].set_xlabel("Integer of BI-RADS Class")

ax[0][1].grid(alpha=0.2)
ax[0][1].hist(data[:,1],edgecolor="black")
ax[0][1].set_title(" patient's age in years (integer)")
ax[0][1].set_xlabel("age [Years]")
ax[0][1].set_ylabel("number of instances")

my_data = data[:,2]
my_data[np.isnan(my_data)] = -1
labels, counts = np.unique(my_data, return_counts=True)
ax[1][0].grid(alpha=0.2)
ax[1][0].bar(labels[1:], counts[1:], align='center',edgecolor="black")
ax[1][0].set_xticks(labels[1:])
ax[1][0].set_title("Shape (nominal)")
ax[1][0].set_ylabel("number of instances")
ax[1][0].set_xlabel("Integer Shape Class")

my_data = data[:,3]
my_data[np.isnan(my_data)] = -1
labels, counts = np.unique(my_data, return_counts=True)
ax[1][1].grid(alpha=0.2)
ax[1][1].bar(labels[1:], counts[1:], align='center',edgecolor="black")
ax[1][1].set_xticks(labels[1:])
ax[1][1].set_title("Margin (nominal)")
ax[1][1].set_ylabel("number of instances")
ax[1][1].set_xlabel("Integer Margin Class")

my_data = data[:,4]
my_data[np.isnan(my_data)] = -1
labels, counts = np.unique(my_data, return_counts=True)
ax[2][0].grid(alpha=0.2)
ax[2][0].bar(labels[1:], counts[1:], align='center',edgecolor="black")
ax[2][0].set_xticks(labels[1:])
ax[2][0].set_title("Density (ordinal)")
ax[2][0].set_ylabel("number of instances")
ax[2][0].set_xlabel("Integer Density Class")

my_data = data[:,5]
labels, counts = np.unique(my_data, return_counts=True)
ax[2][1].grid(alpha=0.2)
ax[2][1].bar(labels[:], counts[:], align='center',edgecolor="black")
ax[2][1].set_xticks(labels[:])
ax[2][1].set_title("Severity (binominal)")
ax[2][1].set_ylabel("number of instances")
ax[2][1].set_xlabel("Severity ")

plt.savefig('Mammograph.pdf')