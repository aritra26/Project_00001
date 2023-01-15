#!/usr/bin/env python
# coding: utf-8

# In[13]:


def dist_val(time1, value1, time2, value2, sig):
    import numpy as np
    from scipy.stats import ks_2samp, norm
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    statistic, pvalue = ks_2samp(value1, value2)
    
    if (pvalue<sig):
        print('The sets does not identify the same variable.')
    else:
        print('Both the sets identify the same variable.')

    # Create a figure and axes for the two histograms and curves
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Create the first histogram
    ax1.hist(value1, bins = 10, density=True, alpha=0.5, color='blue')
    ax1.set_xlabel('Data')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Dataset 1')

    # Create the second histogram
    ax2.hist(value2, bins = 10, density=True, alpha=0.5, color='red')
    ax2.set_xlabel('Data')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Dataset 2')

    # Show the plot
    plt.show()

