from time import time
from sklearn.metrics import f1_score
from sklearn.cross_validation import train_test_split
from sklearn import grid_search, metrics
from sklearn import tree

# split data and print results via p_func
def split_data(x_all, y_all, p_func):
    num_test = int(0.3 * x_all.shape[0])
    X_train, X_test, y_train, y_test = train_test_split(x_all, y_all, test_size=num_test, random_state=0)
    # Show the results of the split
    if(p_func != None):
        p_func("Training set has {} samples.".format(X_train.shape[0]))
        p_func("Testing set has {} samples.".format(X_test.shape[0]))
    return X_train, X_test, y_train, y_test, x_all.shape[0] - num_test


# traint classifier, X_train - train dataset, y_train - labels, p_func - log function
def train_classifier(clf, X_train, y_train, p_func):
    ''' Fits a classifier to the training data. '''
    # Start the clock, train the classifier, then stop the clock
    start = time()
    clf.fit(X_train, y_train)
    end = time()
    # Print the results
    if (p_func != None):
        p_func("Trained model in {:.4f} seconds".format(end - start))


# predict labels with trained classifier clf, p_func - log function
def predict_labels(clf, features, target, p_func, label):
    ''' Makes predictions using a fit classifier based on F1 score. '''
    # Start the clock, make predictions, then stop the clock
    start = time()
    y_pred = clf.predict(features)
    end = time()
    # Print and return results
    if (p_func != None):
        p_func("Made predictions in {:.4f} seconds.".format(end - start))
    score = f1_score(target.values, y_pred, average='weighted', labels=['0', '1', '2', '4', '5'])
    score2 = f1_score(map(only0and1, target.values), map(only0and1, y_pred) , average='weighted', labels=['0', '1'])
    score3 = \
        f1_score(map(_0and1and2, target.values), map(_0and1and2, y_pred) , average='weighted', labels=['0', '1', '2'])
    if (p_func != None):
        # log results
        p_func("F1[0, 1, 2, 4, 5] score for " + label + ": {:.4f}.".format(score))
        p_func("F1[good, bad] score for " + label + ": {:.4f}.".format(score2))
        p_func("F1[good, snow, bad] score for " + label + ": {:.4f}.".format(score3))

def train_predict(clf, X_train, y_train, X_test, y_test, p_func):
    ''' Train and predict using a classifer based on F1 score. '''
    # Indicate the classifier and the training set size
    if (p_func != None):
        p_func("Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train)))
    # Train the classifier
    train_classifier(clf, X_train, y_train, p_func)
    predict_labels(clf, X_train, y_train, p_func, "training set")
    predict_labels(clf, X_test, y_test, p_func, "test set")


# used for evaluation of results in predict_labels, map labels to {0, 1} set
def only0and1(x):
    if x == 5:
        return 1
    else:
        return 0

# used for evaluation of results in predict_labels, map labels to {0, 1, 2} set
def _0and1and2(x):
    if x == 5:
        return 2
    if x == 0 or x == 1:
        return 0
    if x == 2 or x == 4:
        return 1