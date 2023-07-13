import numpy as np

class NewtonException(Exception):
    """
    A class to throw when the second order derivative is zero. 
    """

    def __str__(self):
        return str('second order derivative is zero') 

class Newton(object):
    def __init__(self):
        pass

    def minimize_f1(self, x0, n):
        '''
        Task 1
        x0: starting point x_0
        n: number of iterations
        return: x_n
        '''

        return x0
    
    def minimize_f2(self, x0, n):
        '''
        Task 2
        x0: starting point x_0
        n: number of iterations
        return: x_n
        '''

        return x0

    def minimize_f(self, f, x0, n):
        '''
        Task 3
        f: the function to minimize
        x0: starting point x_0
        n: number of iterations
        return: x_n
        '''

        return x0

if __name__ == '__main__':
    pass