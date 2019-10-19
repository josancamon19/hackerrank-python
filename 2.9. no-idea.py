if __name__ == '__main__':
    input()
    arr = input().split()
    A = set(input().split())
    B = set(input().split())
    # print(len([number for number in arr if number in A]) - len([number for number in arr if number in B]))

    # int(True) = 1, int(False) = 0
    # print(([(i in A) - (i in B) for i in arr]))
    print(sum([(i in A) - (i in B) for i in arr]))
