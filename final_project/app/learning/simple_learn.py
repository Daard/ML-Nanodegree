
from sklearn import tree
from train_and_predict import split_data
import parser as p
from train_and_predict import train_predict


# train classifier and print results using p_func
def learn(data, p_func):
    X_all = p.build_for_single(data)
    y_all = p.label(data)
    X_train, X_test, y_train, y_test, train_size = split_data(X_all, y_all, p_func)
    clf = tree.DecisionTreeClassifier(random_state=0, min_samples_split=2, min_samples_leaf=1, max_depth=16, max_leaf_nodes=10)
    train_predict(clf, X_train[:train_size], y_train[:train_size], X_test, y_test, p_func)
    y_pred = clf.predict(X_test)
    errors(data, p_func, y_pred, y_test)
    return clf


# print errors to the log, useful when you try to improve model or classifier
def errors(data, p_func, y_pred, y_test):
    y_test['pred'] = y_pred
    named = p.with_names(data)
    if p_func != None:
        p_func("Errors:\n")
    for index, row in y_test.iterrows():
        if row['label'] != row['pred']:
            s = str(row['label']) + ',' + str(row['pred']) + ',' + named.icol(0).values[index]
            if p_func != None:
                p_func(s)