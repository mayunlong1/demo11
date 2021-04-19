import requests
from bs4 import BeautifulSoup
import keyword
import unittest


class Demo(unittest.TestCase):
    def setUp(self) -> None:
        print(123123)

    def test_case1(self):
        print('test_case')

    def tearDown(self) -> None:
        print('12313132')


if __name__ == '__main__':
    unittest.main()
