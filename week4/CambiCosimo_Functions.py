#Some Functions To help out ML process
import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score, precision_score, recall_score
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE as smote
from statsmodels.stats.outliers_influence import variance_inflation_factor

def import_csv_as_pandadf(fullfilepath): 

    df = pd.read_csv(fullfilepath)
    return df

def import_csv_as_pandadf_noheader(fullfilepath): 

    df = pd.read_csv(fullfilepath, header=None)
    return df

def calc_prevalence(y_actual):
    # this function calculates the prevalence of the positive class (label = 1)
    return (sum(y_actual)/len(y_actual))

def fillna_col(col,fill):
    col = col.fillna(fill)
    return col

def balance_train_df(df,method,lbl):
    rows_pos = df[lbl] == 1
    df_train_pos = df.loc[rows_pos]
    df_train_neg = df.loc[~rows_pos]

    #Choose Between Sub if there are a ton of Postive samples or 
    #Over if there are just a few Positive Samples
    print('Balance Method Selected is ',method)
    
    if method =='Sub': # split the training data into positive and negative
        #put the positive samples into a new set + an equal amount of  negative samples (the dominant class)
        df_train = pd.concat([df_train_pos, df_train_neg.sample(n = len(df_train_pos), random_state = 12)],axis = 0)

    else:
        if method =='Over':
            #put an equal a mount of positive samples into a new set + the negative samples (the dominant class)
            df_train = pd.concat([df_train_neg, df_train_pos.sample(n = len(df_train_neg), replace = True, random_state = 12)] ,axis = 0)

        else:
            if method =='Smote':
                #Oversampeling the less dominant by Synthetic Minority Over-sampling Technique
                sm = smote(random_state=12)
                input_col = list(df.columns)
                input_col.remove(lbl)
                X=df[input_col].values
                y=df[lbl].values
                train_res, y_res = sm.fit_resample(X,y)
                df_x = pd.DataFrame(train_res, columns = input_col)
                df_y = pd.DataFrame(y_res, columns = [lbl])
                df_train = pd.concat([df_x, df_y], axis=1, sort=False)
            else:
                print('Balancing method not recognized, options are Sub, Over or Smote')
                df_train = df

    # shuffle the new training sample set
    df_train.sample(n = len(df_train), random_state = 12).reset_index(drop = True)


    print('Train balanced prevalence(n = {:0,d}):{:.3f}'.format(len(df_train), calc_prevalence(df_train[lbl])))
    return df_train

def calc_specificity(y_actual, y_pred, thresh):
    return sum((y_pred < thresh) & (y_actual == 0)) /sum(y_actual ==0)

def print_report(y_actual, y_pred, thresh):   
    auc = roc_auc_score(y_actual, y_pred)
    accuracy = accuracy_score(y_actual, (y_pred > thresh))
    recall = recall_score(y_actual, (y_pred > thresh))
    precision = precision_score(y_actual, (y_pred > thresh))
    specificity = calc_specificity(y_actual, y_pred, thresh)
    print('AUC:{:.3f}'.format(auc))
    print('accuracy:{:.3f}'.format(accuracy))
    print('recall:{:.3f}'.format(recall))
    print('precision:{:.3f}'.format(precision))
    print('specificity:{:.3f}'.format(specificity))
    print('prevalence:{:.3f}'.format(calc_prevalence(y_actual)))
    print(' ')
    return auc, accuracy, recall, precision, specificity 

def print_report_ovo(y_actual, y_pred, thresh):   
    auc = roc_auc_score(y_actual, y_pred,multi_class ='ovo')
    print('AUC:{:.3f}'.format(auc))
    print(' ')
    return auc

def fill_w_mean(main,columns):
    imp = SimpleImputer(missing_values=np.nan,strategy='mean')
    imp.fit(main[columns])
    main[columns] = imp.transform(main[columns])
    return main[columns]

def CleanAndConvertToNumeric(col):
    col = [np.nan if x == -9 or x == 9 or x == '?' or x == '9' or x == '-9'
                  else x
                    for x in col]
    col = pd.to_numeric(col, errors='coerce')
    return col

def UniqueValues(df,maxval):
    for c in list(df.columns):

        # get a list of unique values
        n = df[c].unique()

        # if number of unique values is less than maxval, print the values. Otherwise print the number of unique values
        if len(n)<maxval:
            print(c)
            print(n)
        else:
            print(c + ': ' +str(len(n)) + ' unique values')
    #return 0


def Train_Valid_Test_Split(df,seed,tr):
    #First Shuffle the data
    df = df.sample(n = len(df), random_state=seed)
    df = df.reset_index(drop = True)

    #Splits Training Data = tr% - Validation & Test = (1-tr)/2
    #First take (1-tr) for Validation and Test
    valid_test=df.sample(frac=(1-tr),random_state=seed)

    #Then Split the validation and test data in half 
    valid = valid_test.sample(frac=0.50,random_state=seed)
    test = valid_test.drop(valid.index)

    #The remodeling data is use for training data
    train=df.drop(valid_test.index)
    
    return train, valid, test

def calc_vif(X):
    # Calculating VIF
    vif = pd.DataFrame()
    vif["variables"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif = vif.sort_values(by=['VIF'], ascending=False)
    return(vif)

def auto_vif(df,vif_max):
    # Iterate through the columns in the dataframe untill the overall VIF is bellow the input max
    col = list(df.columns)
    vif = calc_vif(df)
    while vif.iloc[0].VIF>vif_max:
        print("Removed column '{}' with a {} VIF.".format(vif.iloc[0].variables,vif.iloc[0].VIF))
        col.remove(vif.iloc[0].variables)
        vif = calc_vif(df[col])
    print("Final VIF DF")
    print(vif)
    return col