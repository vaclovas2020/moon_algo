import math
import json

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

Year = int(input('Year: '))

HowManyYears = int(input('How many years: '))

MoonMonthStart = int(input('Moon month start: '))
MoonYearStart = int(input('Moon year start: '))

LeapYear = False

Data = []

MoonMonthStart -= 1

for Y in range(Year, Year + HowManyYears):
    if Y != 2026:
        Done = True
    else:
        Done = False
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
            Day=math.ceil(calculate_moon_phase(Y,M,D))
            if Day == 1:
                if Done or MoonMonthStart != 2:
                    MoonMonthStart += 1
                else:
                    Done = True
                Data.append({'Year':Y,'Month':M,'Day':D,'MoonMonth':MoonMonthStart,'MoonYear':MoonYearStart,'MoonDay':Day})
            if MoonMonthStart == 12:
                MoonMonthStart = 0
                MoonYearStart += 1
print(json.dumps(Data, indent=4))