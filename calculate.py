import math


def calculate_moon_phase(Y: int, M: int, D: int) -> float:
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
    return S % 29.5305882


Year = int(input("Year: "))

HowManyYears = int(input("How many years: "))

MoonMonthStart = int(input("Moon month start: "))
MoonYearStart = int(input("Moon year start: "))

LeapYear = False

Data = []

MoonMonthStart -= 1

DiffYears = [2023, 2026, 2029, 2032]

for Y in range(Year, Year + HowManyYears):
    try:
        DiffYears.index(Y)
        Done = False
    except ValueError:
        Done = True
    if Y % 4 == 0:
        LeapYear = True
        if Y % 100 == 0:
            LeapYear = False
            if Y % 400 == 0:
                LeapYear = True

    if LeapYear:
        Days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for M in range(1, 13):
        for D in range(1, Days[M - 1] + 1):
            Day = math.ceil(calculate_moon_phase(Y, M, D))
            if Day == 1:
                if Done or MoonMonthStart != 2:
                    MoonMonthStart += 1
                else:
                    Done = True
                Data.append(
                    {
                        "Year": Y,
                        "Month": M,
                        "Day": D,
                        "MoonYear": MoonYearStart,
                        "MoonMonth": MoonMonthStart,
                        "MoonDay": Day,
                        "DaysDiff": Days[M - 1] - D + 1,
                    }
                )
            if MoonMonthStart == 12:
                MoonMonthStart = 0
                MoonYearStart += 1


def DateMinusOneDay(Year: int, Month: int, Day: int) -> tuple:
    if Day == 1:
        if Month == 1:
            Year -= 1
            Month = 12
        else:
            Month -= 1
        Day = Days[Month - 1]
    else:
        Day -= 1
    return (Year, Month, Day)


for i in range(len(Data)):
    if i + 1 < len(Data):
        (NextYear, NextMonth, NextDay) = DateMinusOneDay(
            Data[i + 1]["Year"], Data[i + 1]["Month"], Data[i + 1]["Day"]
        )
    else:
        (NextYear, NextMonth, NextDay) = DateMinusOneDay(
            Data[i]["Year"], Data[i]["Month"], Days[Data[i]["Month"] - 1] + 1
        )
    print(
        f"new HeavenlyCalendarMonth(new GregorianCalendar({Data[i]['Year']}, {Data[i]['Month'] - 1}, {Data[i]['Day']}), new GregorianCalendar({NextYear}, {NextMonth - 1}, {NextDay}), {Data[i]['MoonYear']}, {Data[i]['MoonMonth']}, {Data[i]['DaysDiff']}),"
    )
