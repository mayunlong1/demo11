import pytest
from selenium import webdriver

#
# @pytest.mark.parametrize("a, b, c", [[1,1,1],[2,2,2]])
# def test_ceshiren(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
#
# def test_txkt():
#     caps = {}
#
#     driver = webdriver.Remote('http://182.92.129.158:5001/wd/hub', caps)
#     dr
#     driver.maximize_window()
#     driver.get('https://ke.qq.com/?tuin=62382059')
#     driver.save_screenshot('txkt.png')
#     driver.execute_script()
#     driver.quit()
# #
#
# class TestDemo:
#     @pytest.mark.parametrize('a, b, expect', [1, 2, 3], [100, 100, 100])
#     def test_demo(self, a, b, expect):
#         print(a, b, expect)
from pytest_testconfig import config


class TestDemo:
    def setup(self):
        print('setup')

    def test_a(self):
        print(1111)

    def teardown(self):
        print('teardown')