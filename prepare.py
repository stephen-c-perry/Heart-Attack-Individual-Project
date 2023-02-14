import pandas as pd
from sklearn.model_selection import train_test_split


#rename columns in heart.csv
def rename_cols(df):
    df = df.rename(columns= {'exang': 'exercise_induced_ang',
                              'cp' : 'chest_pain_type',
                              'trtbps' : 'resting_bp',
                              'chol': 'cholesterol',
                              'fbs': 'fasting_blood_sugar>120',
                              'restecg': 'rest_ecg',
                              'thalachh' : 'max_heart_rate',
                              'exng': 'exercise_induced_angina',
                              'slp' : 'st_slope',
                              'caa': 'num_major_blood_vessels',
                              'thall': 'defect_type',
                              'output': 'high_risk_of_mi'})
    return df



#mapping int values in categorical columns to strings for clearer exploration and vizualization
def replace_cat_values(df_strings):

    df_strings['sex'] = df_strings['sex'].replace(0,'female').replace(1, 'male')

    df_strings['chest_pain_type'] = df_strings['chest_pain_type'].replace(0,'asymptomatic').replace(1,'typical angina').replace(2,'atypical angina').replace(3,'non-anginal pain')

    df_strings['fasting_blood_sugar>120'].astype(bool)

    df_strings['rest_ecg'] = df_strings['rest_ecg'].replace(0,'normal').replace(1,'ST-T wave abnormal').replace(2,'left ventricular hypertrophy')

    df_strings['st_slope'] = df_strings['st_slope'].replace(0,'unsloping').replace(1,'flat').replace(2,'downsloping')

    df_strings['defect_type'] = df_strings['defect_type'].replace(0, None).replace(1,'fixed_defect').replace(1,'fixed_defect').replace(2,'normal').replace(3,'reversible')

    df_strings = df_strings.dropna()
    
    return df_strings




def split_data(df, strat= None):
    '''
    take in a DataFrame and return train, validate, and test DataFrames.
    return train, validate, test DataFrames.
    '''
    train_validate, test = train_test_split(df, test_size=.16, random_state=123, stratify=df[strat])
    train, validate = train_test_split(train_validate,
                                       test_size=.2, 
                                       random_state=123, 
                                       stratify=train_validate[strat])
    return train, validate, test