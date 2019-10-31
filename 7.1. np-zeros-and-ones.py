import numpy as np

if __name__ == '__main__':
    inp = tuple(map(int, input().split()))

    print(np.zeros(inp, int))
    print(np.ones(inp, int))
