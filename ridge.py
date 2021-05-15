from sklearn import linear_model
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostRegressor

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data_collection/consolidated_data_bare.csv', index_col=[0], parse_dates=True, infer_datetime_format=True)
# shape(1918, 4)

df = df[:-200]
df_train = df[:-200]
df_test =  df[-200:]

def print_shapes():
    print(df_train.shape)
    print(df_test.shape)

print_shapes()
print(df_test.head)

# visualise data
def visualise_data():
    x_range = range(1, 1719)
    y_btc = df_train['px']
    y_goog = df_train['google_trend']
    y_twit = df_train['twitter_sent']

    fig, axs = plt.subplots(3)
    axs[0].plot(x_range, y_btc)
    axs[1].plot(x_range, y_goog)
    axs[2].plot(x_range, y_twit)

    plt.show()


# print df summary
def print_summary():
    print('train size: ', df_train.shape)
    print('test size: ', df_test.shape)
    print(df.head)
    print(df.dtypes)
    print(df.isnull().sum())

# split into x, y
x_train = df_train[['google_trend', 'twitter_sent']]
x_test = df_test[['google_trend', 'twitter_sent']]
y_train = df_train['px']
y_test = df_test['px']

clf = linear_model.BayesianRidge(compute_score=True)
clf.fit(x_train, y_train)

eln = linear_model.ElasticNet()
eln.fit(x_train, y_train)

svr = svm.SVR(kernel='linear')
svr.fit(x_train, y_train)

y_clf = clf.predict(x_test)
y_eln = eln.predict(x_test)
y_svr = svr.predict(x_test)

def visualise_predictions():
    x_test_range = range(1, 201)

    plt.plot(x_test_range, y_clf, label='br')
    plt.plot(x_test_range, y_eln, label='eln')
    plt.plot(x_test_range, y_svr, label='svr')
    plt.plot(x_test_range, y_test, label='actual')


    plt.legend()
    plt.show()

visualise_predictions()

# k-fold cross validation scoring without adaboost, k = CV_NUM
CV_NUM = 5

cv_scores_clf = cross_val_score(clf, x_train, y_train, cv=CV_NUM, scoring='neg_root_mean_squared_error')
cv_scores_eln = cross_val_score(eln, x_train, y_train, cv=CV_NUM, scoring='neg_root_mean_squared_error')
cv_scores_svr = cross_val_score(svr, x_train, y_train, cv=CV_NUM, scoring='neg_root_mean_squared_error')

print('bayesian ridge: ', cv_scores_clf.mean())
print('elasticnet: ', cv_scores_eln.mean())
print('svr: ', cv_scores_svr.mean())

# adaboosting
# NUM_EST = 5

# for NUM_EST in range(1,50):
#     clf_adb = AdaBoostRegressor(svr, n_estimators=NUM_EST)
#     clf_adb.fit(x_train, y_train)

#     # adaboost scoring
#     cv_scores_clf_adb = cross_val_score(clf_adb, x_train, y_train, cv=CV_NUM, scoring='neg_root_mean_squared_error')
#     print('==============================')
#     print('num_est: ', NUM_EST)
#     print('adaboosted BR: ', cv_scores_clf_adb.mean())
