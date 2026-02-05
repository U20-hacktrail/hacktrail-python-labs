'''IF  anum is divided by 3 print fuzz 
if a number is divisible  by 5 print buzz
if a number is divisible by both print both fuzzbuzz'''
for num in range(1,100):
    if num%3==0 and num%5==0:
        print("fuzzbuzz")
    elif num%3==0:
         print("fuzz")
    elif num%5==0:
        print("buzz")
    else:
        print(num)