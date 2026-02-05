# unit = input("Enter the TB or GB advertised units").strip().lower()
# if unit == 'tb':
#     discrepancy = 1000000000000 / 1099511627776
# elif unit == 'gb':
#     discrepancy = 1000000000 / 1073741824
# else:
#     raise ValueError("Invalid unit, Enter Tb or Gb ")
# advertised_capacity=input ("Enter the  advertised capacity")
# advertised_capacity= float( advertised_capacity)
# real_capacity =str(round(advertised_capacity*discrepancy, 2))
# print('The actual capacity is  ' + real_capacity  + '' + unit)
# 3
#9.  Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = 2
if spam ==1:
    print("Hello")
elif spam ==2:
    print("Howdy")
else:
    print("Gretting")

