

import pytest

from pageObjects.LoginPage import Login
from utilities.Logger import LogGenerator

class Test_CredKart_Login:
    log=LogGenerator.loogen()

    @pytest.mark.sanity()
    def test_pagetitle_1(self,setup):
        self.driver=setup

        ####### log level example ################
        self.log.debug("this is debug")
        self.log.info("this is info")
        self.log.warning("this is warning")
        self.log.error("this is error")
        self.log.critical("this is critical")
        ####################################################

        self.log.info("Started testcases test_pagetitle_1")
        self.log.info("Opening the browser")
        self.log.info("Checking the page title:",str(self.driver.title))

        if self.driver.log=="CredKart":
            self.driver.save_screenshot(".Screenshots\\test_pagetitlt_1_pass.PNG")
            self.log.info("Taking the screenshot")
            self.driver.close()
            self.log.info("Tastcases test_pagetitlt_1 passed ")
            assert True

        else:
            self.driver.save_screenshot(".Screenshots\\test_pagetitlt_1_fail.PNG")
            self.log.info("Taking the screenshot")
            self.driver.close()
            self.log.info("Tastcases test_pagetitlt_1 failed ")
            assert False

        self.log.info("Tastcases test_pagetitlt_1 completed")

    @pytest.mark.sanity
    def test_CredKart_login(self,setup):
        self.driver=setup
        self.log.info("Stared test cases test_CredKart_login")
        self.log.info("Open browser")
        self.lpo=Login(self.driver)


        # self.driver.get("https://automation.credence.in/login")
        self.lpo.click_login_link()
        self.log.info("Click on login link")

        # self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        self.lpo.enter_email("Credencetest@test.com")
        self.log.info("Entering email")

        # self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
        self.lpo.enter_password("Credence@123")
        self.log.info("Entering password")

        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.lpo.clicl_loginbutton()
        self.log.info("Click on login button")

        # print(self.lp.Login_Status()
        if self.lpo.login_status=="True":
            self.driver.save_screenshots(".\\Screenshots\test.CredKart_login_pass.PNG")
            self.log.info("Taking Screenshots")
            self.log.info("Test CredKart_login_ passed")
            assert True
        else:
        self.driver.save_screenshots(".\\Screenshots\test.CredKart_login_fail.PNG")
        self.log.info("Taking Screenshots")
        self.log.info("Test CredKart_login_ Failed")
        assert False
    self.log.info("Testcase test_CredKart_login is Completed")




# pytest -v -s --html=Reports/myreport.html --alluredir="AllureReports" -n=2  testCases/test_Login.py --browser chrome
# testcases
# Cross Browser -- with changing code, now we change the browser with command line
# Metadata for html report pytest-metadata
# Parameterized (Test Data) testcases
# Page objects --> we are defining the all the activities/operations
# Data Driven testing with openpyxl (Excel sheet Test Data)
# logging object -->

# pytest -m "markername" -- > this will run the testcases having given marker name
# example pytest -m "sanity"--> this will run only the sanity marker testcases
# example pytest -m "sanity and regression"--> this will run only the sanity and regression both marker testcases
# example pytest -m "sanity or regression"--> this will run the testcases either having marker sanity or  regression.


# Today's task :
# How to remove warning from console output, search command for it ?
# How to register marker in pytest (https://docs.pytest.org/en/stable/how-to/mark.html) ?


# CT#15 --> sunday monday no class
# CT#14 --> class HR session
# From Tuesday --> we're going start the framework from scratch with theory notes