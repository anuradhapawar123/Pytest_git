

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_CredKart_CheckOut:

    def test_AmountVerification(self, setup):
        self.driver = setup

        #----------Open url---------------
        self.driver.get("https://automation.credence.in/login")

        #------------------Enter Email------------------

        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")

        #------------------Enter password---------------
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")

        # --------------Click Login button----------------
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)


        #----------------click on product macbook---------------
        self.driver.find_element(By.XPATH,"//img[@src='https://automation.credence.in/img/macbook-pro.jpg']").click()

        #------------Add to cart product macbook------------------
        self.driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
        time.sleep(5)

        #---------------click on continouse shopping-----------
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Continue Shopping']").click()

        #------------click on headphone-----------------
        self.driver.find_element(By.XPATH,"//img[@src='https://automation.credence.in/img/headphones.jpg']").click()

        #----------------click on add to cart-------------
        self.driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
        time.sleep(5)


        #---------------click on continouse shopping-----------
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Continue Shopping']").click()

        #------------click on Ipad-----------------
        self.driver.find_element(By.XPATH,"//img[@src='https://automation.credence.in/img/ipad-retina.jpg']").click()

        #----------------click on add to cart-------------
        self.driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
        time.sleep(5)


        # -------------Select Quality dropdown value for product 1(macbook)

        product_quantity1=Select(self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/select[1]"))
        product_quantity1.select_by_index(3)
        time.sleep(2)


        # -------------Select Quality dropdown value for product 2(Headphone)

        product_quantity1=Select(self.driver.find_element(By.XPATH,"//body[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/select[1]"))
        product_quantity1.select_by_index(3)
        time.sleep(2)


        # -------------Select Quality dropdown value for product 3(Apple Ipad)

        product_quantity1=Select(self.driver.find_element(By.XPATH,"//tbody/tr[3]/td[3]/select[1]"))
        product_quantity1.select_by_index(2)
        time.sleep(2)


        l=len(self.driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))
        # l=6
        time.sleep(2)

        product_price_list=[]
        for x in range(1,l-2):

            var1=self.driver.find_element(By.XPATH,"//tbody//tr[" + str(x) + "]//td[4]").text
        #    print(var1)             # $934.5567
            product_price=(var1[1:])   # remove $ from price e.g 934.5567
            print(product_price)
            product_price_list.append(float(product_price))           # convert in float
        print(product_price_list)


        subtotal=round(sum(product_price_list),2)
        # Exp_Subtotal-->11999.889999999998
        # Exp_Subtotal-->11999.89
        print("Subtotal:-",str(subtotal))


        system_value=[]
        for x in range(l-2,l+1):
            var2=self.driver.find_element(By.XPATH,"//tbody//tr[" + str(x) + "]//td[4]").text
            print(var2)   # $11,232.456
            var3=var2.replace(",","")     # $11232.456
            system_price = (var3[1:])      # 11232.456
            system_value.append(float(system_price))    # convert into float

        print(system_value)

        if subtotal == system_value[0]:
            print("SubTotal is matched")
        else:
            print("Subtotal is not matched")
            self.driver.close()

        # self.driver.get("https://automation.credence.in/login")
        #
        # self.driver.get("https://automation.credence.in/login")
        # self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        # self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
        # # Click Login button
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #
        # # Click on Product--Macbook
        # self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3").click()
        # # Click on add to cart
        # self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # # Click on Continue Shopping
        # self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        # # Click on Product--Headphone
        # self.driver.find_element(By.XPATH, "//h3[normalize-space()='Headphones']").click()
        # # Click on add to cart
        # self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # # Click on Continue Shopping
        # self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        # # Click on Product--Ipad
        # self.driver.find_element(By.XPATH, "//h3[normalize-space()='Apple iPad Retina']").click()
        # # Click on add to cart
        # self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # # Select Quality dropdown value for product 1
        # time.sleep(5)
        # product_quantity1 = Select(self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select"))
        # product_quantity1.select_by_index(3)
        # time.sleep(2)
        # # Select Quality dropdown value for product 2
        # product_quantity2 = Select(self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select"))
        # product_quantity2.select_by_index(3)
        # time.sleep(2)
        # # Select Quality dropdown value for product 3
        # product_quantity3 = Select(self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select"))
        # product_quantity3.select_by_index(2)
        #
        # l = len(self.driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))
        # # l=6
        # time.sleep(2)
        # Product_Price_List = []
        # for r in range(1, l - 2):
        #     var1 = self.driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
        #     # print(var1) Var1 = $9,899.10
        #     product_price = (var1[1:])
        #     # print(product_price)
        #     Product_Price_List.append(float(product_price))
        #
        # print(Product_Price_List)
        # Exp_Subtotal = round((sum(Product_Price_List)), 2)
        # # Exp_Subtotal-->11999.889999999998
        # # Exp_Subtotal-->11999.89
        # print("Exp_Subtotal-->" + str(Exp_Subtotal))
        # print(Product_Price_List)
        #
        # System_Value = []
        #
        # for r in range(l - 2, l + 1):
        #     var2 = self.driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text  # $10,499.94
        #     var3 = var2.replace(',', '')  # $10499.94
        #     system_price = (var3[1:])  # 10499.94
        #     System_Value.append(float(system_price))
        #
        # print(System_Value)
        #
        # if Exp_Subtotal == System_Value[0]:
        #     print("SubTotal is matched")
        # else:
        #     print("Subtotal is not matched")
        #     self.driver.close()
        # # Open browser
        # # Url
        # # Login
        # # add product in cart
        # # verify the amount
