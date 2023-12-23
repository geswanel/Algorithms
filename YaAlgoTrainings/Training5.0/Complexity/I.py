"""
Choose day of the week with max and min holidays during the year

INPUT:
N - number of country holidays
year
N lines with country holidays in 
    "day month" format day - number, month - month name
firstJan - name of day

calendar module
    mdays
    month_name
    day_name
    isleap

Will create myself
"""
def isLeap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthId = {
    "January": 0,
    "February": 1,
    "March": 2,
    "April": 3,
    "May": 4,
    "June": 5,
    "July": 6,
    "August": 7,
    "September": 8,
    "October": 9,
    "November": 10,
    "December": 11
}
dayName = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def getDayName(dayPos, janFirst):
    global dayName
    return dayName[(dayPos - 1 + dayName.index(janFirst)) % 7]

def chooseDay(countryHolidays, year, janFirst):
    global mdays
    cntMax = {"cnt": 0, "dId": 0}
    cntMin = {"cnt": 367, "dId": 0}
    mdays[1] += isLeap(year)
    for startDay in range(1, 8):
        cnt = 0
        mId = 0
        newDay = startDay
        while mId < 12:
            if mId not in countryHolidays or newDay not in countryHolidays[mId]:
                cnt += 1
            
            newDay += 7
            if newDay > mdays[mId]:
                newDay %= mdays[mId]
                mId += 1
        
        if cnt > cntMax["cnt"]:
            cntMax["cnt"] = cnt
            cntMax["dId"] = startDay

        if cnt < cntMin["cnt"]:
            cntMin["cnt"] = cnt
            cntMin["dId"] = startDay
    
    return getDayName(cntMax["dId"], janFirst), getDayName(cntMin["dId"], janFirst)


def main():
    N = int(input())
    year = int(input())

    countryHolidays = dict()
    for _ in range(N):
        day, month = input().split()
        mId = monthId[month]

        if mId not in countryHolidays:
            countryHolidays[mId] = set()
        countryHolidays[mId].add(int(day))

    janFisrt = input()

    best, worst = chooseDay(countryHolidays, year, janFisrt)
    print(best, worst)


if __name__ == "__main__":
    main()