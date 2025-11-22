# Q - Create a framework base counter that counts test execution instances:



class TestExecution:
    test_counter=0
    def __init__(self):
        TestExecution.test_counter += 1
        print("test execution count - ",TestExecution.test_counter)


Test1 = TestExecution()
Test2= TestExecution()
Test3= TestExecution()









