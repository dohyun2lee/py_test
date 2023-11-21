year = int(input())

def korean_age(a) :
    from datetime import datetime
    today = datetime.today()
    print(today.year - year + 1)

korean_age(year)