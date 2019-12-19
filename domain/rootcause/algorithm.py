import requests


def analysis(content):
    # should mock
    return False


def rest_call(id):
    return requests.get(url="http://localhost:8000/", params={"id": id}).text
