# Problem description
# Find out if there are any duplicate urls used in the
# json placeholder photo data

import requests

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()
    assert "Presidents of the United States" in rsp_data["Heading"]


def test_ddg1():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()
    assert "Joe Biden" in str(rsp_data["RelatedTopics"])


def test_ddg2():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()
    assert "https://en.wikipedia.org/wiki/Presidents_of_the_United_States" in rsp_data["AbstractURL"]
