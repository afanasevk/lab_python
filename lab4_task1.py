import json


# TODO решите задачу
def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    total = sum(i['score'] * i['weight'] for i in data)

    return round(total, 3)


print(task())

