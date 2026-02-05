''''
Question 1: Login Attempt Analyzer (SOC-style)
Scenario
You’re writing a basic authentication check for a security tool.
Requirements
Take input:
username
password
otp_code
Logic:If username is "admin":
If password is "root123":
If otp_code is "999999":
print "Full access granted"
Else:
Print "Invalid OTP"
Else:
Print "Incorrect password"
Else:
Print "Unknown user"
Constraints
Use nested if statements only
Strip whitespace from inputs
No shortcuts like and chaining everything in one line
This mirrors how layered auth checks are automated before SIEM logging.'''


username =input("Enter your username").strip()
password =input("Enter your password").strip()
otp_code =input("Enter your otp_code").strip()
if username == "admin":
    if password == "root123":
        if otp_code == "999999":
            print("Full access granted")
        else:
            print ("Incorrect password")
    else:
            print  ("Invalid OTP") 
else:
         print ("Unknown user")






