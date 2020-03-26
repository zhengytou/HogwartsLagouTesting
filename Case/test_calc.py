import pytest
from Case.func import Calc

calc = Calc()
print(calc)
add_list = [(1, 99, 100), (-1, -99, -100), (-1, 88, 87), (-1, 1, 0)]
div_list = [(9, 3, 3), (10, 3, 3.33), (5, 10, 0.5), (-9, 3, -3), (10, -3, -3.33), (-5, 10, 0.5), (-9, -3, 3)]

#
# @pytest.mark.parametrize("a,b,result", add_list)
# def test_add(a, b, result):
#     assert calc.add(a, b) == result
# @pytest.mark.parametrize("user,pwd",[("18221124104",111111),("18200000000",111111)])
# def test(user,pwd):
#     print(user,pwd)

class TestCalc(object):
    @pytest.mark.parametrize("a,b,result", add_list)
    def test_add(self, a, b, result):
        assert calc.add(a, b) == result

    @pytest.mark.parametrize("a,b, result", div_list)
    def test_div(self, a, b, result):
        assert calc.div(a, b) == result
