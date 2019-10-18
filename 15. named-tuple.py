from collections import namedtuple

if __name__ == '__main__':
    iters, cols = int(input()), input().split()
    Student = namedtuple('Student', cols)
    print(sum([float(Student._make(input().split()).MARKS) for _ in range(iters)]) / iters)
