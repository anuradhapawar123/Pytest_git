

class Test_arithmatic:

    def test_pro1(self):
        a = 3
        b = 7
        product = a * b
        print("Product of a and b is :" + str(product))
        if product == 21:
            assert True
        else:
            assert False

    def test_sub2(self):
        a = 12
        b = 7
        sub = a - b
        print("Subtraction of a from b is :" + str(sub))
        if sub == 5:
            assert True
        else:
            assert False



# pytest -v --html=HTML reports/myreport.html --alluredir="allure-results" -n=2 TestCases/test_file_4.py