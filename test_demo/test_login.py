import yaml


def test_ddddd():
    data = yaml.safe_load(open('data.yaml', encoding='utf-8'))
    print(data['ck17']['token'])