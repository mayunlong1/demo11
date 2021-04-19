import requests


def test_jinhsuju():

    url = f'https://hogwarts.jinshuju.net/api/v1/forms/ymyq94/entries?next=51'
    r = requests.get(url, auth=('2bJy7M7nXpE5t72lAIe66A', 'Iu09gVMAE4Mdy1Byo75auw'))
    print(r.json())
