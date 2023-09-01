import math

def calculate_moon_phase(Y,M,D):
    C = E = JD = B = A = F = 0
    if M < 3:
        Y -= 1
        M += 12
    A = int(Y / 100)
    B = int(A / 4)
    C = 2 - A + B
    E = int(365.25 * (Y + 4716))
    F = int(30.6001 * (M + 1))
    JD = C + D + E + F - 1524.5
    S = JD - 2451549.5
    return S % 29.53

Y = int(input('Y'))
M = int(input('M'))
D = int(input('D'))

print('Days since New Moon:' + math.ceil(calculate_moon_phase(Y,M,D)))
