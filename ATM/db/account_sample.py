import json
acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 30000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0
}

# print(json.dumps(acc_dic))
with open("1234.json","w") as f:
    json.dump(acc_dic,f)