
import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class Test_Credence_2:
#    @pytest.mark.skip
    def test_credkart_login(self):

        driver = webdriver.Chrome()
        driver.maximize_window()

        # --------------Go to URL--------------

        driver.get("https://automation.credence.in/")
        time.sleep(2)

        # -------------click login hyperlink------------

        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)

        # ---------------------Enter Email----------------

        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@credence.in")
        time.sleep(2)

        # -------------------Enter password-------------------

        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("test@123")
        time.sleep(2)

        # ---------------click login button------------

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        # -------------verifing login status--------------

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")

            print("Login testcase is passed")
            assert True
            driver.close()

        except NoSuchElementException:
            print("Login testcase is failed")
            driver.close()
            assert False





    @pytest.mark.Credence
    def test_amount_verification(self):

        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")

        # ----------------open browser----------------
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.maximize_window()

        # ----------Open url---------------
        driver.get("https://automation.credence.in/login")

        # ------------------Enter Email------------------

        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")

        # ------------------Enter password---------------
        driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")

        # --------------Click Login button----------------
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        # ----------------click on product macbook---------------
        driver.find_element(By.XPATH, "//img[@src='https://automation.credence.in/img/macbook-pro.jpg']").click()

        # ------------Add to cart product macbook------------------
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(5)

        # ---------------click on continouse shopping-----------
        driver.find_element(By.XPATH, "//a[normalize-space()='Continue Shopping']").click()

        # ------------click on headphone-----------------
        driver.find_element(By.XPATH, "//img[@src='https://automation.credence.in/img/headphones.jpg']").click()

        # ----------------click on add to cart-------------
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(5)

        # ---------------click on continouse shopping-----------
        driver.find_element(By.XPATH, "//a[normalize-space()='Continue Shopping']").click()

        # ------------click on Ipad-----------------
        driver.find_element(By.XPATH, "//img[@src='https://automation.credence.in/img/ipad-retina.jpg']").click()

        # ----------------click on add to cart-------------
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(5)

        # -------------Select Quality dropdown value for product 1(macbook)

        product_quantity1 = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select[1]"))
        product_quantity1.select_by_index(3)
        time.sleep(2)

        # -------------Select Quality dropdown value for product 2(Headphone)

        product_quantity1 = Select(
            driver.find_element(By.XPATH, "//body[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/select[1]"))
        product_quantity1.select_by_index(3)
        time.sleep(2)

        # -------------Select Quality dropdown value for product 3(Apple Ipad)

        product_quantity1 = Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select[1]"))
        product_quantity1.select_by_index(2)
        time.sleep(2)

        l = len(driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))
        # l=6
        time.sleep(2)

        product_price_list = []
        for x in range(1, l - 2):
            var1 = driver.find_element(By.XPATH, "//tbody//tr[" + str(x) + "]//td[4]").text
            #    print(var1)             # $934.5567
            product_price = (var1[1:])  # remove $ from price e.g 934.5567
            print(product_price)
            product_price_list.append(float(product_price))  # convert in float
        print(product_price_list)

        subtotal = round(sum(product_price_list), 2)
        # Exp_Subtotal-->11999.889999999998
        # Exp_Subtotal-->11999.89
        print("Subtotal:-", str(subtotal))

        system_value = []
        for x in range(l - 2, l + 1):
            var2 = driver.find_element(By.XPATH, "//tbody//tr[" + str(x) + "]//td[4]").text
            print(var2)  # $11,232.456
            var3 = var2.replace(",", "")  # $11232.456
            system_price = (var3[1:])  # 11232.456
            system_value.append(float(system_price))  # convert into float

        print(system_value)

        if subtotal == system_value[0]:
            print("SubTotal is matched")
            assert True
        else:
            print("Subtotal is not matched")
            assert False


    @pytest.mark.Credence

    def test_credkart_checkout(self):

        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

        # -----------------------open browser-----------

        # driver = webdriver.Chrome()
        driver.maximize_window()

        # ----------------go to url----------------------

        driver.get("https://automation.credence.in/login")

        # ------------------Enter Email------------------

        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")

        # ------------------Enter password---------------
        driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")

        # --------------Click Login button----------------
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        # ----------------click on product macbook---------------
        driver.find_element(By.XPATH, "//img[@src='https://automation.credence.in/img/macbook-pro.jpg']").click()

        # ------------Add to cart product macbook------------------
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(5)

        # ---------------click on continouse shopping-----------
        driver.find_element(By.XPATH, "//a[normalize-space()='Continue Shopping']").click()

        # ------------click on headphone-----------------
        driver.find_element(By.XPATH, "//img[@src='https://automation.credence.in/img/headphones.jpg']").click()

        # ----------------click on add to cart-------------
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(5)

        # -----------proceed to checkout ------------------------
        driver.find_element(By.XPATH, "//a[normalize-space()='Proceed to Checkout']").click()
        time.sleep(2)

        # ------------Enter first name------------------
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Anuradha")

        # ------------Enter last name------------------
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Pawar")

        # ------------Enter phone---------------
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("8937237233")

        # ------------Enter address------------------
        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Sambhajinagar Satara")

        # ------------Enter zip code------------------
        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("415004")

        time.sleep(2)
        # ------------Enter state------------------
        state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        state.select_by_visible_text("Pune")

        # ------------Enter owner------------------
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Anuradha")

        time.sleep(2)
        # ------------Enter CVV------------------
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("567")

        time.sleep(2)
        # ------------Enter card no------------------5281 0370 4891 6168
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")

        # -------------------Enter year------------------
        year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        year.select_by_visible_text("2027")

        # --------------------Enter month------------------
        year = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        year.select_by_visible_text("March")
        time.sleep(2)

        # -----------------click on checkout button------------------

        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()

        print(driver.find_element(By.XPATH, "//div[@class='container text-center']").text)

        time.sleep(5)










