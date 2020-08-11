
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import svm

def classify_svc_lin(features_train, labels_train):

    ### create classifier
    clf = svm.SVC(kernel="linear")

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    return clf

def classify_svc_rbf(features_train, labels_train):

    ### create classifier
    clf = svm.SVR()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    return clf

# получаем выса интервала
def get_interval_weight(interval):
    weight = 0
    num = int(len(interval)/2)
    goal = interval[num][2]
    if (goal == 1):
        return 1
    return weight

def get_interval_weight_cont(interval):
    weight = 0
    for point in interval:
        if (point[2]!=0):
            weight += point[2]
    return weight

# получаем массив весов по массиву интервалов
def get_intervals_weights(interval_list):
    weights = list()
    for i in range(0, len(interval_list)):
        # create_plot(train_interv[i], "interval" + str(i) +".png")
        weights.append(get_interval_weight(interval_list[i]))
    return weights

