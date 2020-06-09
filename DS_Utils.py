import pandas as pd
from fastai.tabular import *

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

def PreprocessWithFastAI(cat_cols, num_cols, X_train,X_test):
    


    fMiss_tfm = FillMissing(cat_cols, num_cols, fill_strategy= FillStrategy.MEDIAN)
    fMiss_tfm.apply_train(X_train)
    fMiss_tfm.apply_test(X_test)

    cat_tfm = Categorify(cat_cols, num_cols)
    cat_tfm.apply_train(X_train)
    cat_tfm.apply_test(X_test)
    for col in cat_cols:
        X_train[col] = X_train[col].cat.codes
        X_test[col] = X_test[col].cat.codes



    norm_tfm = Normalize(cat_cols, num_cols)
    norm_tfm.apply_train(X_train)
    norm_tfm.apply_test(X_test)

    return X_train, X_test