def hyp(X,theta):
    return X*theta[0:2]+theta[2:3]*(X*theta[3:5])
