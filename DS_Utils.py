import pandas as pd


def plotMissingValuesDF(df, percentage = True):
    '''df is a dataframe we want to plot the missing values of, sorted by columns'''
    missingValuesofDF = df.isnull().sum()
    missingValuesofDF = missingValuesofDF[missingValuesofDF>0]
    missingValuesofDF.sort_values(inplace=True, ascending = False)

    if percentage == True:
        missingValuesofDF = missingValuesofDF/df.shape[0]

    missingValuesofDF.plot.bar()



def dropColumnsAbovePercentage(df, percentage = 0.8):
    ''' Takes a dataframe and checks how many missing values there are in it. Then drops all the columns that do not have it. '''
    NrMissing = df.isnull().sum()
    dropColms = NrMissing[NrMissing/df.shape[0] > percentage].index
    if len(dropColms) > 0: 
        print(f'Cut off percentage is set to {percentage}. Dropping columns: {dropColms}')
        return df.drop(columns = dropColms, axis = 1)
    else: 
        print(f'Cut off percentage is set to {percentage}. Dropping no columns as condition is not met')
        return None 