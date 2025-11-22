# 🎯 Goal:
#
# Create a simple automation structure that uses:
#
# A BaseTest class for setup/teardown (Parent class)
#
# A LoginTest class that inherits BaseTest (Child class)
#
# Encapsulate sensitive data (like credentials) as private variables
#
#
# ✅ Requirements:
#
# Create a BaseTest class:
#
# Has a protected variable _driver = "Chrome".
#
# Method setup() prints "Launching browser: Chrome".
#
# Method teardown() prints "Closing browser".
#
# Create a LoginTest class that inherits BaseTest:
#
# Has private variables for username and password.
#
# Method run_test() that prints:
#
# "Running login test with user: <username>".
#
# Use encapsulation: access private vars only through a method (e.g., get_user()).
#
# Create an object of LoginTest and call:
#
# setup()
#
# run_test()
#
# teardown()


class BaseClass():
    _driver="Chrome"

    def setup(self):
        print("Launching browser: Chrome")

    def teardown(self):
        print("Closing browser")

class LoginTest(BaseClass):
        __username="admin"
        __password="Testit123!"

        def getUser(self):
            print("Username is ",LoginTest.__username)

login = LoginTest()
login.setup()
login.teardown()
login.getUser()





















