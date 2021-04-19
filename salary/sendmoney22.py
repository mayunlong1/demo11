from salary import money

paid = 1000


def send_money():
    money.deposit = money.deposit + paid
    print("发工资啦")
    print("余额：", money.deposit)
