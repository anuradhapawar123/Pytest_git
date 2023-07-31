

# config interpreter
# pip install selenium
# pip install pytest - for test run
# pip install pytest-html - to generate report
# pip install pytest-xdist - to run parallel
# pip install allure-pytest - to generate allure report
# Select pytest as default runner in python (Go to setting --> Tools-->integrated Tools
#  to run specific file with abs file path --> pytest -v -n=4 --html=Report/myreport.html "D:\Credence Class Notes
# \CredenceBatches\CredenceBatch#14 & 15\Pytest_July\test_file_002.py"


# file name should start with test_
# class name should start with Test_
# testcases should start with  test_

# To run the test files from terminal--> pytest
# For more details on lib/ plugins--> pytest -v
# For printing the output on console --> pytest -s
# To run specific file in project dir --> pytest filename.py (eg. pytest test_file_001.py)
# To run testcases parallel --> pytest -n=number (eg. pytest -n=2) number--> worker processor
# To generate html report --> (pytest --html=Reports/report.html)
# To set marker for testcases use @pytest.marker.marker_name before testcase
# to run testcases with use define marker--> pytest -m credence


import allure
from selenium import webdriver
import pytest

class Test_credence_1:
    def test_sum_1(self):
        a=20
        b=5
        sum = a+b
        print("Sum of a & b is:", sum)
        print("Sum of a & b is:",str(sum))
        if sum==25:
            assert True
        else:
            assert False

    def test_sum_2(self):
        a=10
        b=9
        sum = a+b
        print("Sum of a & b is:", sum)
        print("Sum of a & b is:",str(sum))
        if sum==25:
            assert True
        else:
            print("Sum is wrong, calculate it one more time")
            assert False

    def test_credence_url1(self):
        driver=webdriver.Chrome()

        driver.get("https://credence.in/")
        if driver.title=="Credence":
            print("You are in Credence.in")
            assert True
            driver.close()
        else:
            print("You are at wrong url")
            driver.close()
            assert False

    @pytest.mark.xfail
    def test_sub1(self):
        a=15
        b=20
        sub=a-b
        print("The substraction  a from b is :",sub)
        print("The substraction  a from b is :",str(sub))
        if sub==-5:
            assert True
        else:
            assert False
