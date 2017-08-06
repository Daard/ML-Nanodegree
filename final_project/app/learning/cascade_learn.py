from train_and_predict import split_data
import parser as p
from train_and_predict import train_tune_predict
from sklearn.metrics import f1_score

# param_grid = {'min_weight_fraction_leaf': [0.1,0.25,0.5],
#               'max_depth':[1,2,4,8],
#               'max_leaf_nodes':[2,5,10],
#               'min_samples_split':[2,5,10]
#               }

def learn(data, p_func):

    new_data = p.add_labels(data)

    X_all = p.build_for_cascade(new_data)
    y_all = p.label(new_data, column='bad')
    X_train, X_test, y_train, y_test, train_size = split_data(X_all, y_all, p_func)
    y_train = y_train[:train_size]
    clf1 = train_tune_predict(X_train[:train_size], y_train['bad'], X_test, y_test, p_func)

    good_data = p.remove_bad(new_data)

    X_all = p.build_for_cascade(good_data)
    y_all = p.label(good_data, column='snow')
    X_train, X_test, y_train, y_test, train_size = split_data(X_all, y_all, p_func)
    y_train = y_train[:train_size]
    clf2 = train_tune_predict(X_train[:train_size], y_train['snow'], X_test, y_test, p_func)

    green_data = p.only_green(new_data)

    X_all = p.build_for_cascade(green_data)
    y_all = p.label(green_data, column='label')
    X_train, X_test, y_train, y_test, train_size = split_data(X_all, y_all, p_func)
    y_train = y_train[:train_size]
    clf3 = train_tune_predict(X_train[:train_size], y_train['label'], X_test, y_test, p_func)

    snow_data = p.only_snow(new_data)

    X_all = p.build_for_cascade(snow_data)
    y_all = p.label(snow_data, column='label')
    X_train, X_test, y_train, y_test, train_size = split_data(X_all, y_all, p_func)
    y_train = y_train[:train_size]
    clf4 = train_tune_predict(X_train[:train_size], y_train['label'],
                              X_test, y_test, p_func, labels=['2', '4'], pos_label=4)

    predict(clf1, clf2, clf3, clf4, data=data)

    return clf1, clf2, clf3, clf4

def predict(clf1, clf2, clf3, clf4, data):
    features = p.build_for_single(data)
    y_all = p.label(data)
    final_pred = []
    y_pred1 = clf1.predict(features)
    for index, v1 in enumerate(y_pred1):
        if v1 == 1:
            final_pred.append(5)
        else:
            snow = clf2.predict(features.iloc[[index],:])
            if snow[0] == 1:
                cloudy = clf4.predict(features)
                final_pred.append(cloudy[0])
            else:
                cloudy = clf3.predict(features)
                final_pred.append(cloudy[0])
    print f1_score(y_all.values, final_pred, average='weighted', labels=['0', '1', '2', '4', '5'])
    named = p.with_names(data)
    for index, pred in enumerate(final_pred):
        y = y_all.icol(0).values[index]
        if y != pred:
            s = str(y) + ',' + str(pred) + ',' + named.icol(0).values[index]
            print s


