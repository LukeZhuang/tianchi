import numpy as np
import hypothesis


def f_linear(theta, X, y, end_day, delta):
    theta = np.mat(theta).T
    m = X.shape[0]
    square = np.power(y - X * theta, 2)
    # weight = 100.*np.exp(np.power(X[:, 1] - end_day, 2) / (-2. * delta * delta))
    weight = 1. / (np.power((X[:, 1] - end_day) / 10, 2) + 1)
    J = (0.5 / m) * np.sum(np.array(square) * np.array(weight))
    return J


def fgrad_linear(theta, X, y, end_day, delta):
    theta = np.array([theta]).T
    m = X.shape[0]
    loss = X * theta - y
    # weight = 100*np.exp(np.power(X[:, 1] - end_day, 2) / (-2. * delta * delta))
    weight = 1. / (np.power((X[:, 1] - end_day) / 10, 2) + 1)
    loss_weight = np.matrix(np.array(loss) * np.array(weight))
    grad = (1. / m) * (X.T * loss_weight)
    return np.array(grad.T.tolist()[0])


def f_lsin(theta, X, y):
    theta = np.array([theta]).T
    m = X.shape[0]
    J = (0.5 / m) * np.sum(np.power(y - hypothesis.hyp(X, theta), 2))
    return J


def fgrad_lsin(theta, X, y):
    theta = np.array([theta]).T
    [m, n] = X.shape[0]
    grad_s = np.zeros([m, 2 * n + 1])
    grad_s[:, 0:2] = X
    grad_s[:, 2] = np.sin(X * theta[3:5])
    grad_s[:, 3] = theta[2] * np.cos(X * theta[3:5])
    grad_s[:, 4] = grad_s[:, 3] * X[:, 1]
    h = hypothesis.hyp(X, theta)
    grad = (1. / m) * (grad_s.T * (h - y))
    return np.array(grad.T.tolist()[0])


def eval(theta, X, y):
    return (X * theta - y) / (X * theta + y)
    # return X * theta - y


def f_evaluation(theta, X, y, end_day):
    theta = np.mat(theta).T
    m = X.shape[0]
    square = np.power(eval(theta, X, y), 2)
    # print square
    weight = 1. / (np.power((X[:, 1] - end_day)/10, 2) + 1)
    J = np.sum(np.array(square) * np.array(weight))
    # print J
    return J


def fgrad_evaluation(theta, X, y, end_day):
    theta = np.array([theta]).T
    m = X.shape[0]
    loss = np.matrix(np.array(eval(theta, X, y)) * np.array(2. * y / np.power(X * theta + y, 2)))
    weight = 1. / (np.power((X[:, 1] - end_day)/10, 2) + 1)
    loss_weight = np.matrix(np.array(loss) * np.array(weight))
    grad = X.T * loss_weight
    # print grad.shape
    # print grad
    return np.array(grad.T.tolist()[0])


if __name__ == '__main__':
    # a = np.array([[1], [2], [3]])
    # b = np.array([1, 2, 3])
    # print a
    # print a.sum(0)
    # grad = np.zeros([2 * 2 + 1, 1])
    # grad[0] = 3
    # print grad
    # c = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    # c[:, 1] = np.array([6, 7, 8])
    # print c
    # d = np.array([[4]])
    # print d * c
    # e = np.array([[4], [5], [6]])
    # print a * e
    # a = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    # b = np.array([[2], [5], [4]])
    # print type(a)
    # print type(b)
    # print a * b
    a = np.matrix('1;2;3')
    b = np.matrix('2;3;4')
    print np.matrix(np.array(a) * np.array(b))
