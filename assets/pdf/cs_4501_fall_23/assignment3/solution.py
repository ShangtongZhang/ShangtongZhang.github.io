import numpy as np

class PGD(object):
    def __init__(self):
        pass

    def projection_to_centered_ball(self, x, radius):
        '''
        Projection to centered ball (1pt)
        x: point to be projected
        radius: the radius of the ball
        return: the projection of @x
        '''
        pass

    def projection_to_ball(self, x, c, radius):
        '''
        Projection to ball (1pt)
        x: point to be projected
        c: the center of the ball
        radius: the radius of the ball
        return: the projection of @x
        '''
        pass
    
    def projection_to_column_space(self, x, A):
        '''
        Projection to column space (1pt)
        x: point to be projected
        A: the matrix with full column rank
        return: the projection of @x
        '''
        pass
    
    def projected_gradient_descent(self, f, x0, n, lr, radius):
        '''
        Projected gradient descent, using projection to a centered ball (1pt)
        f: the function to minimize
        x0: starting point x_0
        n: number of iterations
        lr: learning rate
        radius: the radius of the centered ball
        '''
        pass
    
if __name__ == '__main__':
    pass