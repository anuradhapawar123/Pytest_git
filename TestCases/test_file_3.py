

class Test_Credence_2():
    def test_alert(self):

        import time
        from selenium import webdriver
        from selenium.webdriver.common.alert import Alert
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        #   --------------open browser-----------

        driver = webdriver.Chrome()
        driver.maximize_window()

        # ---------------open url--------------------

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)

        # -----------------click 1 alert tab------------

        driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
        time.sleep(2)

        # ------------print alert massage--------------
        print(Alert(driver).text)
        time.sleep(2)

        # -------------accept alert msg(click ok button)--------------
        Alert(driver).accept()
        # Alert(driver).dismiss()
        time.sleep(2)

        # --------------display text msg-----------
        print(driver.find_element(By.CSS_SELECTOR, "#result").text)
        time.sleep(2)

        # -----------------click 2(confirmation) alert tab------------

        driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
        time.sleep(2)

        # ------------print alert massage--------------
        print(Alert(driver).text)
        time.sleep(2)

        # -------------accept alert msg(click ok button)--------------
        # Alert(driver).accept()
        Alert(driver).dismiss()
        time.sleep(2)

        # --------------display text msg-----------
        print(driver.find_element(By.CSS_SELECTOR, "#result").text)
        time.sleep(2)

        # -----------------click 3(prompt) alert tab------------

        driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
        time.sleep(2)

        # ------------print alert massage--------------
        print(Alert(driver).text)
        time.sleep(2)

        # -------------accept alert msg(click ok button)--------------
        Alert(driver).send_keys("Hi,I'm Anuradha")
        Alert(driver).accept()
        # Alert(driver).dismiss()
        time.sleep(2)

        # --------------display text msg-----------
        print(driver.find_element(By.CSS_SELECTOR, "#result").text)
        time.sleep(2)

        driver.close()


    def test_div1(self):
        a = 20
        b = 3

        div=a/b
        try:
            print("a divides b:",div)
        except ZeroDivisionError:
            print("Raised exception ZeroDivisionError")





