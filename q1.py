# #Level 1: Dictionary Fundamentals
user ={
    "name" : "Ali",
    "age" : 10,
    "is_eligible" : "true"
}
user["age"] = 23
user["email"] = "ali@gmail.com"
print(user  )
email = user.get("email")
print(email)

#Problem 2: Safe Access
 #Tasks
#Try to access "timeout" using .get().
#If "timeout" is missing, print "Using default timeout".
#Concepts Tested
#.get() method
#Avoiding KeyError
config = {
    "host": "localhost",
    "port": 8080,
 }
timeout = config.get("timeout")
print(timeout)

# Problem 3: Loop Through Dictionary
subjects = {
    "maths" : 43,
    "science" :76,
    "practical" : 87,
    
}
for subject,value in subjects.items():
    print(subject, "->", value)

# Problem 4: Conditional Logic
 
# Tasks
# Print names of users who are 18 or older.
# Count how many users are minors.
# Concepts Tested
# Conditionals inside loops 
# Counters 
users = {
    "alice": 25,
    "bob": 17,
    "charlie": 30,
}
for user, value in users.items():
    if int(value) >= 18:
        print(user, value)