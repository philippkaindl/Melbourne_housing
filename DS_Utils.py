import pandas as pd


def plotMissingValuesDF(df):
    '''df is a dataframe we want to plot the missing values of, sorted by columns'''
    missingValuesofDF = df[df.isnull().sum() > 0]
    missingValuesofDF.sort_values(inplace=True, reversed = True)
    missingValuesofDF.plot.bar()