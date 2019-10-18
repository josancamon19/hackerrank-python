# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:

# size 3
#
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
#
# size 5
#
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
#
# size 10
#
# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------
import string
from math import ceil


def print_rangoli(size):
    alphabet = list(string.ascii_lowercase)[:size]

    if size == 1:
        print(alphabet[0])
        return
    if size >= 27:
        size = 26

    height = 2 * size - 1
    width = len('-'.join(alphabet) + '-' + '-'.join(alphabet[1:]))

    for i in reversed(range(1, int(ceil(height / 2)))):
        print(('-'.join(reversed(alphabet[i:])) + '-' + '-'.join(alphabet[i + 1:(height - i)])).center(width, '-'))
    for i in range(int(ceil(height / 2))):
        print(('-'.join(reversed(alphabet[i:])) + '-' + '-'.join(alphabet[i + 1:(height - i)])).center(width, '-'))


if __name__ == '__main__':
    # n = int(input())
    print_rangoli(27)
