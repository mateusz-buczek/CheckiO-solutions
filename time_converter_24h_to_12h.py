#!/usr/bin/env checkio --domain=py run time-converter-24h-to-12h

# https://py.checkio.org/mission/time-converter-24h-to-12h/

# You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
# - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
# - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
# Here you can find some useful information about the12-hour format.
# 
# 
# 
# Input:Time in a 24-hour format (as a string).
# 
# Output:Time in a 12-hour format (as a string).
# 
# Precondition:
# '00:00'<= time<= '23:59'
# 
# 
# END_DESC

def time_converter(time):
    hour = time[0:2]
    if int(hour) >= 12:  # checking if time is PM
        if hour == '12':  # for 12 there is no need to change digits so only add pm
            time = time + ' p.m.'
        else:
            time = time.replace(hour, str(int(hour) - 12), 1)  # change to 12-hour system and add pm
            time = time + ' p.m.'
    else:
        time = time + ' a.m.'  # for am hours add am
        if hour == '00':  # switch to 12 for 00 am
            time = time.replace(hour, '12', 1)

    if int(time[0]) == 0:  # eliminating initial zeros
        return time[1:]

    return time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
