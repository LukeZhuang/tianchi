import numpy as np
import hypothesis

def f(theta,X,y):
    m=X.shape[0]
    J=(1./m)*((y-hypothesis.hyp(X,theta))**2).sum(0)
    return J

def fgrad(theta,X,y):
    [m,n]=X.shape[0]
    grad_s=np.zeros([m,2*n+1])
    grad_s[:,0:2]=X
    grad_s[:,2]=np.sin(X*theta[3:5])
    grad_s[:,3]=theta[2]*np.cos(X*theta[3:5])
    grad_s[:,4]=grad_s[:,3]*X[:,1]
    h=hypothesis.hyp(X,theta)
    grad=(1./m)*((h-y).T*grad_s).T
    return grad

if __name__ == '__main__':
    a=np.array([[1],[2],[3]])
    b = np.array([1,2,3])
    print a
    print a.sum(0)
    grad = np.zeros([2*2+1,1])
    grad[0]=3
    print grad
    c=np.array([[1,2,3],[2,3,4],[3,4,5]])
    c[:,1]=np.array([6,7,8])
    print c
    d=np.array([[4]])
    print d*c
    e = np.array([[4], [5], [6]])
    print a*e
