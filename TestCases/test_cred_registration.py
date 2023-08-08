



import time
from selenium import webdriver

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


# -------------open browser---------------

# driver = webdriver.Chrome()
# driver.maximize_window()
class Test_CredKart_registration:
    def test_cred_registration(self,setup):
        self.driver=setup                 # open browser

        #--------------Go to URL--------------

        self.driver.get("https://automation.credence.in/")
        #
        #                     OR

        # self.driver.get("https://automation.credence.in/Register")
        time.sleep(2)

        #-------------click registration hyperlink------------

        self.driver.find_element(By.LINK_TEXT,"Register").click()
        time.sleep(2)


        #-----------------Enter name---------------

        self.driver.find_element(By.ID,"name").send_keys("Credence Automation")

        #---------------------Enter Email----------------

        self.driver.find_element(By.NAME,"email").send_keys("Credence1237@test.com")

        #-------------------Enter password-------------------

        self.driver.find_element(By.ID,"password").send_keys("Credence@123")

        #----------------------Enter confirm password-------------

        self.driver.find_element(By.ID,"password-confirm").send_keys("Credence@123")

        #---------------click register button------------

        self.driver.find_element(By.CLASS_NAME,"btn").click()
        time.sleep(5)

        #-------------verifing registration status--------------

        try:
            self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print("Registration Testcase is Passed")
        except NoSuchElementException:
            print("Registration Testcase is not Passed")

        time.sleep(2)

        self.driver.close()



