import numpy as np

def func(x):
        return np.exp(-x**2)
      
def trapezcomp(f, a, b, n):
    """
    INPUTS:
    f:  the function to integrate
    a:  lower bound of integration
    b:  upper bound
    n:  number of panels to create between ``a`` and ``b``
    """

    h = (b - a) / n
    x = a

    In = f(a)
    for k in range(1, n):
        x  = x + h
        In += 2*f(x)

    return (In + f(b))*h*0.5

def romberg(f, a, b, p):
    """
    INPUTS:
    f:  the function to integrate
    a:  lower bound of integration
    b:  upper bound
    p:  number of rows in the Romberg table
    """

    I = np.zeros((p, p))
    for k in range(0, p):
        I[k, 0] = trapezcomp(f, a, b, 2**k)

        for j in range(0, k):
            I[k, j+1] = (4**(j+1) * I[k, j] - I[k-1, j]) / (4**(j+1) - 1)

        print(I[k,0:k+1])

    return I
  
def main():
    I = romberg(func, 0, 3, 5)
    solution = I[4, 4]
    print(solution)

if __name__ == '__main__':
    main()