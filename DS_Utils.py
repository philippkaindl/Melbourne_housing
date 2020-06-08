import pandas as pd


def plotMissingValuesDF(df, percentage = True):
    '''df is a dataframe we want to plot the missing values of, sorted by columns'''
    missingValuesofDF = df.isnull().sum()
    missingValuesofDF = missingValuesofDF[missingValuesofDF>0]
    missingValuesofDF.sort_values(inplace=True, ascending = False)

    if percentage == True:
        missingValuesofDF = missingValuesofDF/df.shape[0]

    missingValuesofDF.plot.bar()