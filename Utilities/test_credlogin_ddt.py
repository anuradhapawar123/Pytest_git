

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


from Utilities import XL_utiles
from Utilities.LoginPageObjectddt import Login


class Test_CredKart_login_ddt():
    Xlpath="C:\\Users\\HP\\PycharmProjects\\Pytest\\TestdataExel\\test_login.xlsx"

    def test_CredKart_login_ddt(self,setup):
        self.driver=setup     # open browser
        self.lpo=Login(self.driver)    # pageobject call
        self.row=XL_utiles.RowCount(self.Xlpath,"sheet1")   # Xl row count
        print("Number of rows in Exel is:" + str(self.row))
        Login_Status_List=[]

        for r in range(2,self.row+1):    # iterate Xl rows
            self.email=XL_utiles.ReadData(self.Xlpath,"sheet1",r,2)     # read email
            self.password = XL_utiles.ReadData(self.Xlpath, "sheet1", r, 3)  # read password
            self.exp_result = XL_utiles.ReadData(self.Xlpath, "sheet1", r, 4)  # read exp result
            self.lpo.click_login_link()
            self.lpo.enter_email()
            self.lpo.enter_password()
            self.lpo.click_loginbutton()

            if self.lpo.login_status==True:
                if self.exp_result=="pass":
                    Login_Status_List.append("pass")
                    self.driver.save_screenshot(".\\Screenshots\\Test_CredKart_login_ddt_pass.PNG")
                    self.lpo.click_menu_button()
                    self.lpo.click_logout_button()
                    XL_utiles.WriteData(self.Xlpath,"sheet1",r,5,"pass")

                elif self.exp_result=="fail":
                    Login_Status_List.append("fail")
                    self.driver.save_screenshot(".\\Screenshots\\Test_CredKart_login_ddt_fail.PNG")
                    self.lpo.click_menu_button()
                    self.lpo.click_logout_button()
                    XL_utiles.WriteData(self.Xlpath,"sheet1",r,5,"fail")

            if self.lp.Login_Status() == False:
                if self.exp_result == "Pass":
                    Login_Status_List.append("Fail")
                    self.driver.save_screenshot(".\\Screenshots\\Test_CredKart_Login_fail.PNG")
                    XL_utiles.WriteData(self.Xlpath, "Sheet1", r, 5, "Fail")
                elif self.exp_result == "Fail":
                    Login_Status_List.append("Pass")
                    XL_utiles.WriteData(self.Xlpath, "Sheet1", r, 5, "Pass")
        print(Login_Status_List)
        if "Fail" not in Login_Status_List:
            assert True
        else:
            assert False















