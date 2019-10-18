from cmath import phase, sqrt, polar


def polar_coordinates(cpx):
    print('{0:.3f}'.format(sqrt(pow(cpx.real, 2) + pow(cpx.imag, 2)).real))
    print('{0:.3f}'.format(abs(phase(complex(cpx.real, cpx.imag)))))


if __name__ == '__main__':
    # polar_coordinates(complex(input()))
    print(*polar(complex(input())), sep='\n')
