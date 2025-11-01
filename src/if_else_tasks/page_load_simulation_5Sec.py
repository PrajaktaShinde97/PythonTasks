# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
#
# Hint: Use a counter (like wait_time) and break condition.

import time
import random
counter=1

while counter<=5:
    choice = random.choice([True, False])
    if choice:
        print("✅ Test Passed")
        break
    else:
        print("⚠️  Page is Loading ")
        time.sleep(1)
        print("Waiting for a second ")
        counter = counter + 1
