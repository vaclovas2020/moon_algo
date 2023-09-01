import math

def calculate_moon_phase(Y: int,M: int,D: int) -> float:
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

Y = int(input('Year: '))

MoonMonthStart = int(input('Moon month start: '))
MoonYearStart = int(input('Moon year start: '))

LeapYear = False

if Y % 4 == 0:
    LeapYear = True
    if Y % 100 == 0:
        LeapYear = False
        if Y % 400 == 0:
            LeapYear = True

if LeapYear:
    Days = [31,29,31,30,31,30,31,31,30,31,30,31]

else:
    Days = [31,28,31,30,31,30,31,31,30,31,30,31]

for M in range(1,13):
    for D in range(1,Days[M-1]+1):
        print(Y,M,D, sep='-',end=' ')
        Day=math.ceil(calculate_moon_phase(Y,M,D))
        if Day == 1 and M != 1:
            MoonMonthStart += 1
        if MoonMonthStart > 12:
            MoonMonthStart = 1
            MoonYearStart += 1
        print("Moon year:", MoonYearStart, sep=' ',end=' ')
        print("Moon month:", MoonMonthStart, sep=' ',end=' ')
        print("Moon day:",math.ceil(calculate_moon_phase(Y,M,D)), sep=' ')
