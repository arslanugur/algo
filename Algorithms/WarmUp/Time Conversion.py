#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#      - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock
import sys

def timeConversion(s):
    if 'AM' in s:
        s_split = s.replace('AM', '').split(':')
        if s_split[0] == '12':
            s_split[0] = '00'
        res = s_split[0] + ':' + s_split[1] + ':' + s_split[2]
        return res
    else:
        s_split = s.replace('PM', '').split(':')
        
        if s_split[0] != '12':
            s_split[0] = str(int(s_split[0]) + 12)
        res = s_split[0] + ':' + s_split[1] + ':' + s_split[2]
        return res

s = input().strip()
result = timeConversion(s)
print(result)

