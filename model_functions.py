import pandas as pd
import numpy as np
import acquire
import prepare

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


'''
#function for my best performing model
def best_performing_model(X_Train, y_Train, X_test, y_test):
    
    rf = RandomForestClassifier(max_depth=9, min_samples_leaf=3, random_state=123)
    rf.fit(X_Train, y_Train)

    print('Random Forest')
    print(f"Test Accuracy: {rf.score(X_test, y_test):.2%}")
'''

#function to run multiple random forest to compare for best accuracy
def get_decision_tree_multiple(X_Train, y_Train, X_val, y_val):
    metrics = []

    for j in range (1, 10):
        for i in range(2, 10):
            clf = DecisionTreeClassifier(max_depth=i, min_samples_leaf=j, random_state=123)

            clf = clf.fit(X_Train, y_Train)
            in_sample_accuracy = clf.score(X_Train, y_Train)
            out_of_sample_accuracy = clf.score(X_val, y_val)

            output = {
                "min_samples_per_leaf": j,
                "max_depth": i,
                "train_accuracy": in_sample_accuracy,
                "validate_accuracy": out_of_sample_accuracy
            }
    
            metrics.append(output)

    df1 = pd.DataFrame(metrics)
    df1["difference"] = df1.train_accuracy - df1.validate_accuracy
    df1_sorted = df1.sort_values(by=['validate_accuracy'], ascending=False).head(10)

    return df1_sorted



#function to run multiple random forest to compare for best accuracy
def get_random_forest_multiple(X_Train, y_Train, X_val, y_val):
    metrics = []

    for j in range (1, 10):
        for i in range(2, 10):
            rf = RandomForestClassifier(max_depth=i, min_samples_leaf=j, random_state=123)

            rf = rf.fit(X_Train, y_Train)
            in_sample_accuracy = rf.score(X_Train, y_Train)
            out_of_sample_accuracy = rf.score(X_val, y_val)

            output = {
                "min_samples_per_leaf": j,
                "max_depth": i,
                "train_accuracy": in_sample_accuracy,
                "validate_accuracy": out_of_sample_accuracy
            }
    
            metrics.append(output)

    df1 = pd.DataFrame(metrics)
    df1["difference"] = df1.train_accuracy - df1.validate_accuracy
    df1_sorted = df1.sort_values(by=['validate_accuracy'], ascending=False).head(10)

    return df1_sorted






#function run multiple KNN to compare for best accuracy
def get_knn(X_Train, y_Train, X_val, y_val):
    metrics = []

    for i in range(2, 10):
        knn = KNeighborsClassifier(n_neighbors=i, weights='uniform')
        knn = knn.fit(X_Train, y_Train)
        in_sample_accuracy = knn.score(X_Train, y_Train)
        out_of_sample_accuracy = knn.score(X_val, y_val)

        output = {
            "neighbors": i,
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy
        }

        metrics.append(output)

    df1 = pd.DataFrame(metrics)
    df1["difference"] = df1.train_accuracy - df1.validate_accuracy
    df1_sorted = df1.sort_values(by=['validate_accuracy'], ascending=False).head(10)

    return df1_sorted


#isolating target variable in train, validate, test sets
def isolate_target(train, validate, test, target):

    X_Train = train.drop(columns = [target])
    y_Train = train[target]

    X_val = validate.drop(columns = [target])
    y_val = validate[target]

    X_test = test.drop(columns = [target])
    y_test = test[target]
    return X_Train, y_Train, X_val, y_val, X_test, y_test



#get dummies and drop any columns
def df_classification_ready(df, cols= None):
    df = pd.get_dummies(df)
    df = df.drop(columns= [cols])

    return df