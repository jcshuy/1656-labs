import json
from datetime import datetime, timedelta
import requests
import pandas as pd
import numpy as np
from sklearn import linear_model, tree, metrics
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Task(object):

    def __init__(self, bike_df, bank_df):
        np.random.seed(31415)
        self.bike_data = bike_df.sample(1000).copy()
        self.bank_data = bank_df.copy()

    def t1(self):
        df = self.bike_data

        train = df.iloc[0:900]
        train_x = train[['weekday']].values
        train_y = train[['cnt']].values
        test = df.iloc[900:]
        test_x = test[['weekday']].values
        test_y = test[['cnt']].values
        # print(type(train_x), type(train_y), type(test_x), type(test_y))

        # Create linear regression object
        regr = linear_model.LinearRegression()
        # Train the model using the training sets
        regr.fit(train_x, train_y)

        # The coefficients
        print('Coefficients: \n', regr.coef_)

        predict_y = regr.predict(test_x)
        # Printing predicted and actual values side by side fro comparison

        np.column_stack((predict_y, test_y))
        # print(np.column_stack((predict_y, test_y)))

        meansq_error = np.mean((predict_y - test_y)**2)
        # print("Mean squared error: %.2f" % meansq_error)\
        return meansq_error

        # plt.scatter(test_x, test_y, color='black', linewidth=1)
        # plt.plot(test_x, predict_y, color='blue', linewidth=3)
        # plt.show()

    def t2_1(self):
        df = self.bike_data

        train = df.iloc[0:900]
        train_x = train[[
            'season', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit',
            'temp', 'temp_feels', 'hum', 'windspeed'
        ]].values
        train_y = train[['cnt']].values
        test = df.iloc[900:]
        test_x = test[[
            'season', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit',
            'temp', 'temp_feels', 'hum', 'windspeed'
        ]].values
        test_y = test[['cnt']].values
        # print(type(train_x), type(train_y), type(test_x), type(test_y))

        # Create linear regression object
        regr = linear_model.LinearRegression()
        # Train the model using the training sets
        regr.fit(train_x, train_y)

        # The coefficients
        # print('Coefficients: \n', regr.coef_)

        predict_y = regr.predict(test_x)
        # Printing predicted and actual values side by side fro comparison

        np.column_stack((predict_y, test_y))
        # print(np.column_stack((predict_y, test_y)))

        meansq_error = np.mean((predict_y - test_y)**2)
        # print("Mean squared error: %.2f" % meansq_error)
        return meansq_error
        #TASK 2.2 - The mean squared error is lower. It's better to use all attributes as it shows a lower margin of error from the larger input size.

    def t2_2():
        summary = 'abccnmz,z,z,'

        return summary

    def t3(self):
        dt = self.bank_data
        # print(dt.head())
        # print(list(dt.columns))
        #titanic columns only
        #dt['Sex'] = dt['Sex'].replace(['female', 'male'], [1, 2])
        #bank data
        dt['sex'] = dt['sex'].replace(['FEMALE', 'MALE'], [1, 2])
        dt['married'] = dt['married'].replace(['YES', 'NO'], [1, 0])
        dt['mortgage'] = dt['mortgage'].replace(['YES', 'NO'], [1, 0])
        dt['region'] = dt['region'].replace(
            ['INNER_CITY', 'TOWN', 'RURAL', 'SUBURBAN'], [1, 2, 3, 4])

        dt_train_x = dt.iloc[:500][['region', 'sex', 'married']].values
        dt_train_y = dt.iloc[:500][['mortgage']].values
        dt_test_x = dt.iloc[500:][['region', 'sex', 'married']].values
        dt_test_y = dt.iloc[500:][['mortgage']].values

        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(dt_train_x, dt_train_y)

        dt_predict_y = clf.predict(dt_test_x)
        ## comparing predicted and actual values
        np.column_stack((dt_predict_y, dt_test_y))
        # print(np.column_stack((dt_predict_y, dt_test_y)))
        accuracy = metrics.accuracy_score(dt_test_y, dt_predict_y)

        return accuracy


if __name__ == "__main__":
    #pd.read_csv('http://data.cs1656.org/titanic.csv')
    t = Task(pd.read_csv('http://data.cs1656.org/bike_share.csv'),
             pd.read_csv('http://data.cs1656.org/bank-data.csv'))
    print("---------- Task 1 ----------")
    print(t.t1())
    print("--------- Task 2.1 ---------")
    print(t.t2_1())
    print("--------- Task 2.2 ---------")
    #print(t.t2_2())
    print("---------- Task 3 ----------")
    print(t.t3())
