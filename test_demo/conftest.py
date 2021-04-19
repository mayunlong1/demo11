import pytest


def pytest_collection_modifyitems(items):
    print(type(items))  # items是一个列表list
    # items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# @pytest.fixture(scope=)
# def return_value():
#     print("登录")
