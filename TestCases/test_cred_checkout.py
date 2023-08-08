

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from TestCases.test_credlogin import driver


class Test_CredKart_CheckOut:

    def test_AmountVerification(self, setup):
        self.driver = setup

        #-----------------------open browser-----------
        # driver = webdriver.Chrome()
        self.driver.maximize_window()

        #----------------go to url----------------------

        self.driver.get("https://automation.credence.in/login")

        #------------------Enter Email------------------

        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")

        #------------------Enter password---------------
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")

        # --------------Click Login button----------------
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)


        #----------------click on product macbook---------------
        self.driver.find_element(By.XPATH,"//img[@src='https://automation.credence.in/img/macbook-pro.jpg']").click()

        #------------Add to cart product macbook------------------
        self.driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
        time.sleep(2)

        #---------------click on continouse shopping-----------
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Continue Shopping']").click()

        #------------click on headphone-----------------
        self.driver.find_element(By.XPATH,"//img[@src='https://automation.credence.in/img/headphones.jpg']").click()

        #----------------click on add to cart-------------
        self.driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
        time.sleep(2)

        #-----------proceed to checkout ------------------------
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Proceed to Checkout']").click()
        time.sleep(2)

        #------------Enter first name------------------
        self.driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("Anuradha")

        #------------Enter last name------------------
        self.driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("Pawar")

        #------------Enter phone---------------
        self.driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("8937237233")


        #------------Enter address------------------
        self.driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("Sambhajinagar Satara")

        #------------Enter zip code------------------
        self.driver.find_element(By.XPATH,"//input[@id='zip']").send_keys("415004")


        time.sleep(2)
        #------------Enter state------------------
        state=Select(self.driver.find_element(By.XPATH,"//select[@id='state']"))
        state.select_by_visible_text("Pune")

        #------------Enter owner------------------
        self.driver.find_element(By.XPATH,"//input[@id='owner']").send_keys("Anuradha")


        time.sleep(2)
        #------------Enter CVV------------------
        self.driver.find_element(By.XPATH,"//input[@id='cvv']").send_keys("567")

        time.sleep(2)
        #------------Enter card no------------------5281 0370 4891 6168
        self.driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("5281")
        self.driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("0370")
        self.driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("4891")
        self.driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("6168")

        #-------------------Enter year------------------
        year=Select(self.driver.find_element(By.XPATH,"//select[@id='exp_year']"))
        year.select_by_visible_text("2027")

        #--------------------Enter month------------------
        year=Select(self.driver.find_element(By.XPATH,"//select[@id='exp_month']"))
        year.select_by_visible_text("March")
        time.sleep(2)


        # -----------------click on checkout button------------------

        self.driver.find_element(By.XPATH,"//button[@id='confirm-purchase']").click()

        print(self.driver.find_element(By.XPATH, "//div[@class='container text-center']").text)

        time.sleep(2)
        self.driver.close()
