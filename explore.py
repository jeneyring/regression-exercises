import pandas as pd
import matplotlib as plt
import seaborn as sns

import wrangle
import prepare


"""
Explore.py is a file for the Functions for the visualizations of the Zillow dataset
"""

def plot_variable_pairs(train):
    """
    a function that calls in the train zillow dataset and creates a lmplot for the zillow
    continous variables
    """
    columns = ['yearbuilt','taxamount']
    for col in columns:
        sns.lmplot(x= col, y="taxvaluedollarcnt", data=train.sample(1000), col = 'county', hue = 'county', line_kws={'color': 'red'})
        

#____________________________________________________

def plot_categorical_and_continuous_vars(train):
    """
    a function that calls in the train zillow dataset and creates a boxplot, barplot
    violinplot and scatterplot for the zillow categorical variables
    """
    columns = ['bathroomcnt','bedroomcnt']
    for x in columns:
    
        sns.set()
        fig, axes = plt.subplots(2,2)
        sns.boxplot(x= x, y="taxvaluedollarcnt", data=train.sample(1000), hue = 'county', ax = axes[0,0])
        sns.barplot(x= x, y="taxvaluedollarcnt", data=train.sample(1000), hue = 'county', ax = axes[0,1])
        sns.violinplot(x= x, y="taxvaluedollarcnt", data=train.sample(1000), hue = 'county', ax = axes[1,0])
        sns.scatterplot(x= x, y="taxvaluedollarcnt", data=train.sample(1000), hue = 'county', ax = axes[1,1])