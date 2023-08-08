

from selenium.webdriver.common.by import By

class CredKart_Checkout:
    click_macbook_Xpath=(By.XPATH,"//img[@src='https://automation.credence.in/img/macbook-pro.jpg']")
    click_addcart_Xpath1= (By.XPATH,"//input[@value='Add to Cart']")
    click_continous_shpping_Xpath=(By.XPATH,"//a[normalize-space()='Continue Shopping']")
    click_headphone_Xpath=(By.XPATH,"//img[@src='https://automation.credence.in/img/headphones.jpg']")
    click_addcart_Xpath2= (By.XPATH,"//input[@value='Add to Cart']")
    click_proceedcheckout_Xpath=(By.XPATH,"//a[normalize-space()='Proceed to Checkout']")
    enter_firstname_Xpath=(By.XPATH,"//input[@id='first_name']")
    enter_lastname_Xpath=(By.XPATH,"//input[@id='last_name']")
    enter_phone_Xpath=(By.XPATH,"//input[@id='phone']")
    enter_address_Xpath=(By.XPATH,"//textarea[@id='address']")
    enter_zip_Xpath=(By.XPATH,"//input[@id='zip']")
    dropdown_state_Xpath=(By.XPATH,"//select[@id='state']")
    enter_owner_Xpath=(By.XPATH,"//input[@id='owner']")
    enter_cvv_Xath=(By.XPATH,"//input[@id='cvv']")
    enter_cardno_Xpath=(By.XPATH,"//input[@id='cardNumber']")
    dropdown_year_Xpath=(By.XPATH,"//select[@id='exp_year']")
    dropdown_month_Xpath=(By.XPATH,"//select[@id='exp_month']")
    click_checkout_Xpath=(By.XPATH,"//button[@id='confirm-purchase']")
    success_msg_Xpath=(By.XPATH, "//div[@class='container text-center']")

    def __init__(self,driver):
        self.driver = driver
    def click_macbook(self):
        self.driver.find_element(*CredKart_Checkout.click_macbook_Xpath).click()








