import numpy as np

if __name__ == '__main__':
    np.set_printoptions(legacy='1.13')
    n, m = tuple(map(int, input().split()))
    A = np.array([input().split() for _ in range(n)], int)
    print(np.mean(A, axis=1))
    print(np.var(A, axis=0))
    print(np.std(A))
