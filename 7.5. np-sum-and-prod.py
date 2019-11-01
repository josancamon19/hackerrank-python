import numpy as np

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    A = np.array([np.array(input().split(), int) for _ in range(n)])
    print(np.prod(np.sum(A, axis=0)))
