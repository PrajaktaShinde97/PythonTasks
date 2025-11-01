# You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.

api_response = int(input("Enter response code : "))
if api_response == 200:
    print("✅ Passed API Request")
elif api_response == 404:
    print("❌ Failed API Request")
else:
    print("Enter valid api response code.")



