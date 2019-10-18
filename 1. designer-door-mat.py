# https://www.hackerrank.com/challenges/designer-door-mat/

# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. ( N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# Input Format
# A single line containing the space separated values of N and M.

# Output Format
# Output the design pattern.

# Sample Input
# 9 27

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------


def print_door_mat(N, M):
    base = [['-' for i in range(M)] for x in range(N)]
    decorator = '.|.'
    center_word = 'WELCOME'
    for i, row in enumerate(base):

        if i == int(N / 2):
            # put centered word
            w_half_len = int(len(center_word) / 2)
            for j, c in enumerate(row[int(M / 2) - w_half_len: int(M / 2) + w_half_len + 1]):
                row[j + int(M / 2) - w_half_len] = center_word[j]
        else:
            if i > int(N / 2):
                i = N - i - 1
            # print(i)
            # print(int(M/2) - ((i + 1) * len(decorator)) + 2, int(M/2) + ((i + 1) * len(decorator)) - 2)
            start = int(M / 2) - ((i + 1) * len(decorator)) + 2
            end = int(M / 2) + ((i + 1) * len(decorator)) - 1

            dec_idx = 0
            for j, c in enumerate(row[start:end]):

                row[start + j] = decorator[dec_idx]
                dec_idx += 1
                if dec_idx == len(decorator):
                    dec_idx = 0

    for row in base:
        print(''.join(row))
    # for row in base:
    #     print(len(row))


if __name__ == '__main__':
    N, M = 7, 21
    # N, M = input().split()
    print_door_mat(int(N), int(M))