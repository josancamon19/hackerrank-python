if __name__ == '__main__':
    T = [list(map(float, input().split())) for _ in range(int(input().split()[1]))]
    [print(sum(student) / len(student)) for student in list(zip(*T))]
