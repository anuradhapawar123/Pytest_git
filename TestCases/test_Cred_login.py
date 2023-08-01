

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

class Test_CredKart_login():

    def test_pageTitle(self):

        driver.get("https://credence.in/")
        if driver.title == "Credence":
            driver.save_screenshot(".Screenshots//test_pageTitle_pass.PNG")
            print("You are in Credence.in")
            assert True
            driver.close()
        else:
            print("You are at wrong url")
            driver.save_screenshot(".Screenshots//test_pageTitle_fail.PNG")
            driver.close()
            assert False