from datetime import date
from datetime import time
import jpholiday
from datetime import timezone,\
                     timedelta, datetime

t = date.today()
y = date(2023,2,2)
u = time(12, 15, 30, 0)
s = datetime.now()
r = datetime(2023, 7, 13, 22, 11, 11)
r2 = datetime(2023, 7, 13, 22)
r3 = r2.date()
r4 = datetime(2023, 6, 20, 12, 30, 30)
result = r - r4
# rから10日間進めた日にちをresult2に代入
result2 = r + timedelta(days=10)

"""
タイムゾーンについて
協定世界時（UTC）：世界の時間の基準になる時間のこと
日本の時刻より9時間遅い
"""
JST = timezone(timedelta(hours=+9))
result3 = datetime(2023, 1, 1, 12, 15, 30, tzinfo=JST)
print(result)
"""
jpholidayは祝日かどうかを判定するもの
is_holiday：祝日ならTrue それ以外はFalse
is_holiday_name：祝日の名前を表示
yaer_holidays：datetimeオブジェクトと祝日の名前がタプルで表示
"""
d = datetime(2021, 5, 3)
result4 = jpholiday.is_holiday(d)
result5 = jpholiday.is_holiday_name(d)

result6 = jpholiday.year_holidays(2023)


print(t)
print(y)
# 3は木曜日
print(y.weekday())
print(u)
print(s)
print(s.year, s.month, s.day)
print(s.hour, s.minute, s.second, s.microsecond)
print(r)
print(r2)
print(r3)
print(result)
print(result.days)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)