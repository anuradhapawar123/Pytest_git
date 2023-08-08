

import time
from selenium.webdriver.common.by import By

class Login:
    enter_email_Css=(By.CSS_SELECTOR,"input[type='email']")
    enter_password_Css=(By.CSS_SELECTOR,"input[name='password']")
    click_loginbutton_Css=(By.CSS_SELECTOR,"button[type='submit']")
    login_status_Css=(By.CSS_SELECTOR, "div[class='jumbotron text-center clearfix'] h2")

    def __init__(self,driver):
        self.driver = driver

    def login_url(self):
        self.driver.get("https://automation.credence.in/login")
        time.sleep(2)

    # def login_hyperlink_link(self):
    #    self.driver.find_element(*Login.click_login_hyperlink_link).click()

    def enter_email(self,email):
        self.driver.find_element(*Login.enter_email_Css).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*Login.enter_password_Css).send_keys(password)

    def click_loginbutton(self):
        self.driver.find_element(*Login.click_loginbutton_Css).click()

    def login_status(self):
        try:
            self.driver.find_element(*Login.login_status_Css)
            return True
        except:
            return False






import time

from selenium.webdriver.common.by import By


class Login:
    Text_Email_XPATH = (By.XPATH, "//input[@name='email']")
    Text_Password_CSS = (By.CSS_SELECTOR, "input[id='password']")
    Click_Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    login_status = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def Login_URL(self):
        self.driver.get("https://automation.credence.in/login")

    def Enter_Email(self, email):
        self.driver.find_element(*Login.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Login.Text_Password_CSS).send_keys(password)

    def CLick_Login_Button(self):
        self.driver.find_element(*Login.Click_Login_Button_XPATH).click()

    def Login_Status(self):
        try:
            self.driver.find_element(*Login.login_status)
            return True
        except:
            return False
