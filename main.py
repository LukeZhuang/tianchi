# coding=utf-8
import matplotlib.pyplot as ploter
import numpy as np

import LoadData.loaddata as loader
import TrainData.traindata as trainer
import Performance.evaluation as evaluator

# 全量
# n = 2000
# T = 14
# tot_loss = 0.0
# for shop_id in range(n):
#     for week_day in range(7):
#         print 'shop_id = %d, week_day = %d' % (shop_id + 1, week_day + 1)
#         [trainX, trainy, testX, testy] = loader.loadfromMysql(shop_id + 1, week_day + 1)
#         if testX.shape[0] > 0:
#             theta = trainer.train(trainX, trainy)
#             tot_loss += evaluator.evaluation(testX * theta, testy)
# print 'evaluation = %f' % (tot_loss / (n * T))

# 单个测试
[trainX, trainy, testX, testy] = loader.loadfromMysql(217, 1)
ploter.figure(1)
ploter.plot(np.row_stack((trainX[:, 1], testX[:, 1])), np.row_stack((trainy, testy)), 'b-')
theta = trainer.train(trainX, trainy)
ploter.plot(np.row_stack((trainX[:, 1], testX[:, 1])), np.row_stack((trainX * theta, testX * theta)), 'r-')
ploter.show(1)
