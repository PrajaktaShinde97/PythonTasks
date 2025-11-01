# An API sometimes fails due to network delays.
#
# Write a program to retry the API call 3 times until the response code becomes 200.
#
# If it still fails after 3 tries, print a failure message.
#
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
#
# Expected Output Example:
#
# Attempt 1: Response 500
#
# Attempt 2: Response 200
#
# ✅ Test Passed


counter=1

while counter<=3:
    api_response = int(input("Enter API response code : "))
    if api_response == 200:
        print("✅ Test Passed")
        break
    else:
        counter = counter+1
        print("❌ Test Failed")



