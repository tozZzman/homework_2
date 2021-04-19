import csv
from json import loads, dumps
from copy import deepcopy

books = []
users = []
example = {
  "name": "",
  "gender": "",
  "address": "",
  "books": [
    {
      "title": "",
      "author": "",
      "height": ""
      }

    ]

}

with open(file='books.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for item in reader:
        books.append(dict(zip(header, item)))

with open(file='users.json', mode='r') as file:
    users = loads(file.read())

with open('result.json', mode='w') as file:
    res_msg = {"users_and_books": []}

    if len(books) >= len(users):
        result = list(map(lambda x, y: dict(list(x.items()) + list(y.items())), users, books))
        for item in result:
            message = deepcopy(example)
            message["name"] = item["name"].replace("\'", "")
            message["gender"] = item["gender"].replace("\'", "")
            message["address"] = item["address"].replace("\'", "")
            message["books"][0]["title"] = item["Title"].replace("\'", "")
            message["books"][0]["author"] = item["Author"].replace("\'", "")
            message["books"][0]["height"] = item["Height"].replace("\'", "")
            res_msg["users_and_books"].append(message)

    elif len(books) < len(users):
        i = 0
        for i in range(len(users)):
            message = deepcopy(example)
            message["name"] = users[i]['name'].replace("\'", "")
            message["gender"] = users[i]['gender'].replace("\'", "")
            message["address"] = users[i]['address'].replace("\'", "")
            if i >= len(books):
                message["books"] = []
            else:
                message["books"][0]["title"] = books[i]["Title"].replace("\'", "")
                message["books"][0]["author"] = books[i]["Author"].replace("\'", "")
                message["books"][0]["height"] = books[i]["Height"].replace("\'", "")
            res_msg["users_and_books"].append(message)

    res_msg = str(res_msg).replace("\'", "\"")
    parsed = loads(res_msg)
    file.write(dumps(parsed, indent=4, sort_keys=True))
