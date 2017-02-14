# coding=utf-8
import matplotlib.pyplot as ploter
import numpy as np

import LoadData.loaddata as loader
import TrainData.traindata as trainer
import Performance.evaluation as evaluator
import LoadData.polyX as polyer
import Performance.showresult as showresult


# 全量
def outputall():
    sql_res = loader.loadall()
    n = 2000
    T = 14
    tot_loss = 0.0
    for shop_id in range(n):
        for week_day in range(7):
            print 'shop_id = %d, week_day = %d' % (shop_id + 1, week_day + 1)
            [trainX, trainy, testX, testy] = loader.loadfromMysql(sql_res[week_day], 475)
            if testX.shape[0] > 0:
                theta = trainer.train(trainX, trainy)
                tot_loss += evaluator.evaluation(np.maximum(testX * theta, 0), testy)
    print 'evaluation = %f' % (tot_loss / (n * T))


# 单个测试
def outputone(shop_id, week_day):
    sql_res = loader.loadall(shop_id)
    [trainX, trainy, testX, testy] = loader.loadfromMysql(sql_res[week_day - 1], 475)
    ploter.figure(1)
    ploter.plot(np.row_stack((trainX[:, 1], testX[:, 1])), np.row_stack((trainy, testy)), 'b-')
    theta = trainer.train(trainX, trainy)
    ploter.plot(np.row_stack((trainX[:, 1], testX[:, 1])), np.row_stack((trainX * theta, testX * theta)), 'r-')
    # print theta
    # print testX
    # print testX * theta
    ploter.show(1)


# 最终结果
def finaljob():
    test_day = [[496, 503], [490, 497], [491, 498], [492, 499], [493, 500], [494, 501], [495, 502]]
    n = 2000
    T = 14
    f_out = open('result.csv', 'w')
    for shop_id in range(n):
        sql_res = loader.loadall(shop_id + 1)
        result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for week_day in range(7):
            print 'shop_id = %d, week_day = %d' % (shop_id + 1, week_day + 1)
            [trainX, trainy, testX, testy] = loader.loadfromMysql(sql_res[week_day], 489)
            theta = trainer.train(trainX, trainy)
            # ploter.figure(1)
            # ploter.plot(trainX[:,1],trainy,'b-')
            # ploter.plot(trainX[:,1],trainX*theta,'r-')
            # ploter.show(1)
            testX = np.matrix(np.array(test_day[week_day])).T
            predict = (polyer.polyX(testX) * theta).T.tolist()[0]
            testX = (testX).T.tolist()[0]
            for i in range(len(testX)):
                result[testX[i] - 490] = predict[i]
        print>> f_out, '%d' % (shop_id + 1),
        for i in range(14):
            print >> f_out, ',%d' % (max(int(result[i]), 0)),
        print>> f_out, ''


if __name__ == '__main__':
    # outputall()
    outputone(888, 7)
    # finaljob()
    # showresult.visualizeResult(217)
    # a=np.matrix('1;2;3')
    # a=np.power(a,2)
    # b=np.matrix('2;3;4')
    # print (np.array(a)*np.array(b))
