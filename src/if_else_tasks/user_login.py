# Check if the user can log in based on correct username and password.
username = input("Enter username : ")
password = input("Enter password : ")

if username == "admin" and password == "1234":
    print("✅ Login is successful")
else:
    print("❌ Invalid Credentials")


