#Day1/365 days  of code challenge
#if-else  Practice(Authentication + input validation)
username = input("Enter username:").strip()
password = input("Enter password:").strip()
if username == "admin" and password == "root123":
    print("Access granted")
elif username == "admin" and password != "root123":
    print("Invalid password")
else:
    print("User not found")

payload = input("ENTER PAYLOAD:")
payload_lower =payload.lower()
if "<script>" in payload_lower or "select" in payload_lower or "' or 1=1" in payload_lower:
    print("Possible injection attempt")
elif len(payload)>30:
    print("Input too Long")
else:
    print("Input Accepted:")
    
 #Day1/365 days  of code challenge
#if-else  Practice(Authentication + input validation)
username = input("Enter username:").strip()
password = input("Enter password:").strip()
if username == "admin" and password == "root123":
    print("Access granted")
elif username == "admin" and password != "root123":
    print("Invalid password")
else:
    print("User not found")

payload = input("ENTER PAYLOAD:")
payload_lower =payload.lower()
if "<script>" in payload_lower or "select" in payload_lower or "' or 1=1" in payload_lower:
    print("Possible injection attempt")
elif len(payload)>30:
    print("Input too Long")
else:
    print("Input Accepted:")
 