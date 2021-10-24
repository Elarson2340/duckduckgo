# Problem description
# Find out if there are any duplicate urls used in the
# json placeholder photo data

import requests

url_ddg = "https://api.duckduckgo.com"


def test_Heading():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()
    assert "Presidents of the United States" in rsp_data["Heading"]


