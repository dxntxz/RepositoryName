# TODO решите задачу
import json

file="input.json"

def task() -> float:
    sum_=0
    with open(file, "r") as f:
        data = json.load(f)
        for item in data:
            sum_+=item["score"]*item["weight"]
    return round(sum_, 3)

print(task())
