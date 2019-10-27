if __name__ == '__main__':
    cols = int(input().split()[0])
    students = [list(map(int, input().split())) for _ in range(cols)]
    key_to_sort = int(input())
    sorted_students = sorted(students, key=lambda student: student[key_to_sort])
    print('\n'.join(' '.join(list(map(str, student))) for student in sorted_students))

    # can be reduced to
    # students = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
    # print('\n'.join(' '.join(list(map(str, student))) for student in sorted(students, key=lambda student: student[int(input())])))
