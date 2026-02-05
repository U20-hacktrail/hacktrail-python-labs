# Student Grade Checker Program
# Purpose: Check if student passes based on score, attendance, and assignments
def get_int_input(prompt):
    while True:
        try:
            value =  int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! please enter valid input in numbers")

def get_yes_no_input(prompt):
    while True:
         value = input(prompt).strip().lower()
         if value in ["yes","y"]:
            return True
         elif value in ["no","n"]:
            return False
         else:
              print("Invalid input plz enter yes or no ")     
              #Main program #
name = input("Enter your name: ")
exam_score =get_int_input("Enter your score in exams in between 0 and 100: ")
attendance_percent = get_int_input("Enter your Attendance percentage: ")
assignment_status = get_yes_no_input("Is your assignment completed or pending?answer in yes/no : ")
if exam_score > 100 or exam_score < 0 or attendance_percent > 100 or attendance_percent < 0:
    print("Error: Score and attendance must be between 0 and 100.")
else: 
#decision logic
     if exam_score >= 60:
        if not assignment_status:
                print(f"{name}, you passed the exam but failed due to missing assignments.")
        elif attendance_percent > 85:
            print(f"{name} congrats! you pass with good grades")
        else:
             print(f"{name} U passed! but with low attendance.")
     else:
         print(f"{name}, you failed the exam. Better luck next time.")