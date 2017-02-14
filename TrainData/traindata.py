import numpy as np
import scipy.optimize as opt
import loss as cost

def train(trainX, trainy):
    [m,n]=trainX.shape
    init_theta_linear=np.zeros(n)
    # eps=0.01
    # init_theta_lsin=np.random.rand(n)*(2*eps)-eps
    theta=opt.fmin_cg(cost.f_evaluation,init_theta_linear,fprime=cost.fgrad_evaluation,args=(trainX,trainy,475))
    return np.mat(theta).T


if __name__ == '__main__':
    a=np.random.rand(10)*0.2-0.1
    print a
    for i in range(10):
        print i