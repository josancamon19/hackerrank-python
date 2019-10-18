from datetime import datetime

if __name__ == '__main__':
    dt_format = '%a %d %b %Y %H:%M:%S %z'
    for t_itr in range(int(input())):
        print(int(abs((datetime.strptime(input(), dt_format) - datetime.strptime(input(), dt_format)).total_seconds())))
