# Given the names and grades for each student in a Physics class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade,
# order their names alphabetically and print each name on a new line.
#
# Input Format
#
# The first line contains an integer, N, the number of students.
# The @N  subsequent lines describe each student over 2 lines;
# the first line contains a student's name, and the second line contains their grade.
#
# Constraints
# 2 ≤ N ≤ 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics;
# if there are multiple students, order their names alphabetically and print each one on a new line.

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Berry
# Harry

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    print('\n'.join(sorted([s[0] for s in students if s[1] == sorted(list(set([s[1] for s in students])))[1]])))
