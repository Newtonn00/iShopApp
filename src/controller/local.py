import requests



res = requests.get("http://16.16.251.222:5000/api/order/12")
print(res.json())
# res = requests.get("http://127.0.0.1:5000/api/good/36")
# print(res.json())

# res = requests.delete("http://127.0.0.1:5000/api/order/12")
# print(res.json())
# res = requests.delete("http://127.0.0.1:5000/api/good/36")
# print(res.json())


# res = requests.post("http://127.0.0.1:5000/api/order/0",
#                     json={"order_id": 0,
#                           "created_on": "2023-05-05T18:25:43.511Z",
#                           "status_code": "01",
#                           "city": "Moscow", "amount": 1000, "vat_amount": 200,
#                           "quantity": 15, "weight": 8, "created_by": "user",
#                           "customer_no": "985643",
#                           "items": [{"order_id": 0, "good_id": 5647,
#                                      "item_no": 10,
#                                      "good_name": "laptop", "quantity": 10},
#                                     {"order_id": 0, "good_id": 9647,
#                                      "item_no": 20,
#                                      "good_name": "Chair", "quantity": 2}]})
# print(res.json())



# res = requests.post("http://127.0.0.1:5000/api/good/5",
#                    json={"good_id": 0, "name": "Chair big big",
#                          "availqty": 125, "category": "999", "status_code": "1"})
# print(res.json())

# res = requests.put("http://127.0.0.1:5000/api/good/36",
#                   json={"good_id": 36, "name": "Chair",
#                         "availqty": 55, "category": "19", "status_code": "1"})
# print(res.json())

# res = requests.put("http://127.0.0.1:5000/api/order/23",
#                   json={"order_id": 98564363,
#                         "created_on": "2023-05-05T18:25:43.511Z",
#                         "status_code": "05",
#                         "city": "Moscow", "amount": 1000,
#                         "vat_amount": 200,
#                         "quantity": 15, "weight": 8, "created_by": "user",
#                         "customer_no": "985643",
#                         "items": [{"order_id": 23, "good_id": 5647,
#                                    "item_no": 10,
#                                    "good_name": "laptop", "quantity": 10},
#                                   {"order_id": 23, "good_id": 9647,
#                                    "item_no": 20,
#                                    "good_name": "Chair", "quantity": 2},
#                                   {"order_id": 23, "good_id": 1647,
#                                    "item_no": 30,
#                                    "good_name": "Chair", "quantity": 45}
#                                   ]})
# print(res.json())
