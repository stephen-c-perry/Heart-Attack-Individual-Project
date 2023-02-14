import pandas as pd
import numpy as np
import acquire
import prepare

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier



#function for my best performing model
def best_performing_model(X_Train, y_Train, X_test, y_test):
    
    rf = RandomForestClassifier(max_depth=9, min_samples_leaf=3, random_state=123)
    rf.fit(X_Train, y_Train)

    print('Random Forest')
    print(f"Test Accuracy: {rf.score(X_test, y_test):.2%}")



def decision_tree_results(X_Train, y_Train, X_val, y_val):
    clf = DecisionTreeClassifier(max_depth=3, random_state=123)
    clf.fit(X_Train, y_Train)
    print('Accuracy of Decision Tree classifier on training set: {:.2f}'.format(clf.score(X_Train, y_Train)))
    print('Accuracy of Decision Tree classifier on validate set: {:.2f}'.format(clf.score(X_val, y_val)))
    # print(f"Difference: {(clf.score(X_Train, y_Train)-clf.score(X_val, y_val)):.2%}")



#function to run multiple random forest to compare for best accuracy
def get_random_forest_multiple():
    metrics = []

    for j in range (1, 10):
        for i in range(2, 10):
            rf = RandomForestClassifier(max_depth=i, min_samples_leaf=j, random_state=123)

            rf = rf.fit(X_Train, y_Train)
            in_sample_accuracy = rf.score(X_Train, y_Train)
            out_of_sample_accuracy = rf.score(X_validate, y_validate)

            output = {
                "min_samples_per_leaf": j,
                "max_depth": i,
                "train_accuracy": in_sample_accuracy,
                "validate_accuracy": out_of_sample_accuracy
            }
    
            metrics.append(output)

    df1 = pd.DataFrame(metrics)
    df1["difference"] = df1.train_accuracy - df1.validate_accuracy
    df1.sort_values(by=['validate_accuracy'], ascending=False).head(10)





#function run multiple KNN to compare for best accuracy
def get_knn():
    metrics = []

    for i in range(2, 10):
        knn = KNeighborsClassifier(n_neighbors=i, weights='uniform')
        knn = knn.fit(X_Train, y_Train)
        in_sample_accuracy = knn.score(X_Train, y_Train)
        out_of_sample_accuracy = knn.score(X_validate, y_validate)

        output = {
            "neighbors": i,
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy
        }

        metrics.append(output)

    df1 = pd.DataFrame(metrics)
    df1["difference"] = df1.train_accuracy - df1.validate_accuracy
    df1.sort_values(by=['validate_accuracy'], ascending=False).head(10)




#isolating target variable in train, validate, test sets
def isolate_target():
    df_telco = acquire.get_telco_data()
    df_telco = prepare.prep_telco(df_telco)
    train, validate, test = prepare.split_data(df_telco)

    X_Train = train.drop(columns = ['churn_Yes', 'customer_id'])
    y_Train = train.churn_Yes

    X_val = validate.drop(columns = ['churn_Yes', 'customer_id'])
    y_val = validate.churn_Yes

    X_test = test.drop(columns = ['churn_Yes', 'customer_id'])
    y_test = test.churn_Yes
    return X_Train, y_Train, X_val, y_val, X_test, y_test
        

'''
def get_baseline():
    def isolate_target_2():
        df_telco = acquire.get_telco_data()
        df_telco = prepare.prep_telco(df_telco)
        train, validate, test = prepare.split_data(df_telco)

        X_Train = train.drop(columns = ['churn_Yes', 'customer_id'])
        y_Train = train.churn_Yes

        X_val = validate.drop(columns = ['churn_Yes', 'customer_id'])
        y_val = validate.churn_Yes

        X_test = test.drop(columns = ['churn_Yes', 'customer_id'])
        y_test = test.churn_Yes
        return X_Train, y_Train, X_val, y_val, X_test, y_test
   
    baseline = 1 - y_Train.mean()
    baseline_percent = (baseline*100)
    print(f'baseline equals:  {round(baseline_percent, 2)}%')
'''
