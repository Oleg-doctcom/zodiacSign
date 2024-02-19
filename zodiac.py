def define(day,month):
    zodiac=month
    if day>=1 and day<=31 and month>=1 and month<=12:
        if day>=22:
            zodiac+=1
            if zodiac>12:
                zodiac=1
    else:
        zodiac=0
    return zodiac
print(define(222,122))