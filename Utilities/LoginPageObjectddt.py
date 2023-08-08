
import time

from selenium.webdriver.common.by import By

class Login:
    click_loginbutton_Xpath = (By.XPATH, "//a[normalize-space()='Login']")
    enter_email_Css =(By.CSS_SELECTOR ,"input[type='email']")
    enter_password_Css =(By.CSS_SELECTOR ,"input[name='password']")
    click_loginbutton_Css =(By.CSS_SELECTOR ,"button[type='submit']")
    login_status_Css =(By.CSS_SELECTOR, "div[class='jumbotron text-center clearfix'] h2")
    click_menu_Xpath = (By.XPATH, "//a[@role='button']")
    cLick_logout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")


    def __init__(self ,driver):
        self.driver = driver

    def click_login_link(self):
        self.driver.find_element(*Login.click_loginbutton_Xpath).click()

#    def login_hyperlink_link(self):
#        self.driver.find_element(*Login.click_login_hyperlink_link).click()

    def enter_email(self ,email):
        self.driver.find_element(*Login.enter_email_Css).send_keys(email)

    def enter_password(self ,password):
        self.driver.find_element(*Login.enter_password_Css).send_keys(password)

    def click_loginbutton(self):
        self.driver.find_element(*Login.click_loginbutton_Css).click()

    def login_status(self):
        try:
            self.driver.find_element(*Login.login_status_Css)
            return True
        except:
            return False


    def click_menu_button(self):
        self.driver.find_element(*Login.click_menu_Xpath).click()


    def click_logout_button(self):
        self.driver.find_element(*Login.cLick_logout_Xpath).click()
