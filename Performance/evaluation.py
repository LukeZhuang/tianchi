import numpy as np


def evaluation(predict, testy):
    loss = 0.0
    predict = predict.T.tolist()[0]
    testy = testy.T.tolist()[0]
    for i in range(len(predict)):
        if predict[i] == testy[i]:
            loss += 0
        else:
            loss += abs((predict[i] - testy[i]) / (predict[i] + testy[i]))
    print loss
    return loss
