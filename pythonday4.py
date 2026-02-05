Monday = False
#if say it_is_opposite_day as Monday
if Monday == True:
    say_it_is_opposite_Day = True
else:
    say_it_is_opposite_Day = False
    
#if it is opposite day then toggle into say today is opposite day
if Monday == True:
    say_it_is_opposite_Day = not say_it_is_opposite_Day

if say_it_is_opposite_Day == True:
    print("Today is Monday  ")
else:
    print("Today is not  Monday  ")
    