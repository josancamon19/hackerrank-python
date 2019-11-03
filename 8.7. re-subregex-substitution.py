import re

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))
