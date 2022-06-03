import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt

from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr, spearmanr



"""
A py file that holds the evaluation codes needed for the zillow dataset.
Coded functions include:
- plot_residuals(y, yhat): creates a residual plot 
- regression_errors(y, yhat): returns the following values:
    - sum of squared errors (SSE)
    - explained sum of squares (ESS)
    - total sum of squares (TSS)
    - mean squared error (MSE)
    - root mean squared error (RMSE)
- baseline_mean_errors(y): computes the SSE, MSE, and RMSE for the baseline model
- better_than_baseline(y, yhat): returns true if your model performs better than the baseline, otherwise false
"""

def plot_residuals(df, y, yhat):
    """
    A function that takes in a dataset, y= df.'target_var', yhat
    and return a residuals plot (baseline and model predictor)
    """
    #create a residual columns on df
    df['residual'] = df.y - df.yhat
    #create a baseline_residual
    df['baseline_residual'] = df.y - df.baseline
    
    # residual plots (x vs residual)
    plt.figure(figsize = (11,5))
    plt.subplot(121)
    plt.scatter(df.y, df.baseline_residual)
    plt.axhline(y = 0, ls = ':')
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.title('Baseline Residuals')

    plt.subplot(122)
    plt.scatter(df.y, df.residual)
    plt.axhline(y = 0, ls = ':')
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.title('OLS model residuals');
    return plt.show()

#_______________________________________________

def regression_errors(y, yhat):
    """
    A function that takes in a dataset and creates a regression_errors(y, yhat): 
    and returns the following values:
    - sum of squared errors (SSE)
    - explained sum of squares (ESS)
    - total sum of squares (TSS)
    - mean squared error (MSE)
    - root mean squared error (RMSE)"""
#first calculate the square of residuals (makes it all positive)
    df['residual^2'] = df.residual**2
    SSE = df['residual^2'].sum()
    MSE = SSE/len(df)
    TSS = SSE = df['residual^2'].sum()
    ESS = TSS - SSE
    RMSE = sqrt(MSE)
    
    print("SSE =", "{:.1f}".format(SSE))
    print("MSE = ", "{:.1f}".format(MSE))
    print("TSS = ","{:.1f}".format(TSS))
    print("ESS = ","{:.1f}".format(ESS))
    print("RMSE = ", "{:.1f}".format(RMSE))

#___________________________________________________________

def baseline_mean_errors(y):
    """
    A function that takes in a dataset and creates a baseline_mean_errors(y): 
    and returns the following values:
    - sum of squared errors (SSE)
    - mean squared error (MSE)
    - root mean squared error (RMSE)
    """
#first calculate the baseline square of residuals (makes it all positive)
    df['baseline_residual^2'] = df.baseline_residual**2

#sum of squared errors (SSE)

    SSE_baseline = df['baseline_residual^2'].sum()

#mean squared error (MSE)

    MSE_baseline = SSE_baseline/len(df)

#TOTAL SUM OF SQUARES

    TSS_baseline = SSE_baseline = df['baseline_residual^2'].sum()

#EXPLAINED SUM of SQUARES

    ESS_baseline = TSS_baseline - SSE-baseline

#ROOT MEAN SQUARED ERROR

    RMSE_baseline =  sqrt(MSE_baseline)


print("SSE Baseline =", "{:.1f}".format(SSE_baseline))


print("MSE baseline = ", "{:.1f}".format(MSE_baseline))


print("RMSE baseline = ", "{:.1f}".format(RMSE_baseline))


#_______________________________________________________

def better_than_baseline(y, yhat):

    Baseline = baseline_mean_errors['SSE_baseline','MSE_baseline','RMSE_baseline'].sum()

    Model = regression_errors['SSE','MSE','RMSE'].sum()

    if Baseline > Model: 
        print ('Model beats baseline')
    else:
        print('Baseline beats Model')
