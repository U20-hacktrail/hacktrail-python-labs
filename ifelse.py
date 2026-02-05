score =int (input("Enter your score in exam"))
attendance = int(input("Enter your attendance"))
assignement  = int(input("Enter your assignement marks"))
submitted = True
if score >=60:
	if attendance >= 80:
		print("U pass with good grades")
	else:
		if not submitted:
			print("u missed some imp assignments")
		else:
  			print("u passed with low attendance")
else:
	print("u failed , try better next time")
       
	score = int(input("Enter your score in exam: "))
attendance = int(input("Enter your attendance percentage: "))
assignment = int(input("Enter your assignment marks: "))
submitted = True

if score >= 60:
    if attendance >= 75:
        print("You passed with good grades")
    else:
        if not submitted:
            print("You missed some important assignments")
        else:
            print("You passed with low attendance")
else:
    print("You failed, try better next time")