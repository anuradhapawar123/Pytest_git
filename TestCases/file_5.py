
def test_div1(self):
    a = 2652
    b = 17

    div = a / b
    try:
        print("a divides b:" ,div)
    except ZeroDivisionError:
        print("Raised exception ZeroDivisionError")
