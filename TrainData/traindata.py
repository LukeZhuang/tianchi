import numpy as np
import scipy.optimize as opt
import loss as cost


def train(trainX, trainy):
    [m, n] = trainX.shape
    # init_theta=np.zeros(n)
    # print init_theta
    eps = 1
    min_theta = np.zeros(n)
    minJ = np.inf
    for i in range(20):
        init_theta = np.random.rand(n) * (2 * eps) - eps
        # theta = opt.fmin_cg(cost.f_linear, init_theta, fprime=cost.fgrad_linear, args=(trainX, trainy, 475,1))
        theta = opt.fmin_cg(cost.f_evaluation, init_theta, fprime=cost.fgrad_evaluation, args=(trainX, trainy, 475))
        # theta = opt.fmin_cg(cost.f_evaluation, init_theta, args=(trainX, trainy, 475))
        J = cost.f_evaluation(theta, trainX, trainy, 475)
        if J < minJ:
            minJ = J
            min_theta = theta
    print minJ
    return np.mat(min_theta).T


if __name__ == '__main__':
    a = np.random.rand(10) * 0.2 - 0.1
    print a
    for i in range(10):
        print i
