import numpy as np

def init_fn(d1, d2):
    return np.random.randn(d1, d2)

def sigma_fn(x):
    return 0.5 * np.power(x, 2)

def d_sigma_fn(x):
    return x

def init_W_b(d):
    W = []
    b = []
    n = len(d) - 1
    for i in range(n):
        W.append(init_fn(d[i], d[i+1]))
        b.append(init_fn(d[i+1], 1))
    return W, b

class NeuralNetwork(object):
    def __init__(self, W, b, sigma_fn, d_sigma_fn):
        '''
        W: the sequence W in the PDF
        b: the sequence b in the PDF
        sigma_fn: the activation function
        d_sigma_fn: the derivative of the activation function
        '''
        pass
    
    def forward(self, x):
        '''
        x: the x in the PDF, a numpy array of size (d0, 1)
        @return: f(x;W,b) in the PDF, a numpy array of size (dn, 1)
        '''
        pass

    
    def backward(self, x, y):
        '''
        x: the x in the PDF, a numpy array of size (d0, 1)
        @return: a tuple (dW, db)
            dW is a list. dW[i] stores the gradient of W[i]. dW[i] has the same shape as W[i]. 
            db is similarly defined.
        '''
        pass
        
    
if __name__ == '__main__':
    # The following is an example of how the grader will call your class
    W, b = init_W_b([2, 3, 7, 4])
    nn = NeuralNetwork(
        W=W,
        b=b,
        sigma_fn=sigma_fn,
        d_sigma_fn=d_sigma_fn
    )
    x = np.random.randn(2, 1)
    y = np.random.randn(4, 1)
    dW, db = nn.backward(x, y)
