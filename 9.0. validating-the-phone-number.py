import re

if __name__ == '__main__':
    [print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO') for _ in range(int(input()))]