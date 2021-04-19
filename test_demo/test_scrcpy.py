import os
import time

import pytest
import yaml
from selenium import webdriver


@pytest.mark.parametrize('demo', ['大大', 2, 3])
def test_demo(demo):
    print(demo)



