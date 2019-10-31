import numpy as np

if __name__ == '__main__':
    ls = np.array([np.array(input().split(), int) for _ in range(int(input().split()[0]))])
    print(ls.transpose())
    print(ls.flatten())
