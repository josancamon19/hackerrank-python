import numpy as np

if __name__ == '__main__':
    np.set_printoptions(sign=' ')
    A = np.array(input().split(), float)
    print(np.floor(A))
    print(np.ceil(A))
    print(np.rint(A))
