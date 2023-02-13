import pandas as pd



#acquires csv file from local storage
def get_heart():
    '''
    heart.csv downloaded from this url:
    https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset?select=heart.csv
    '''
    df = pd.read_csv('heart.csv')
    return df


