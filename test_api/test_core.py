import requests

def test_httpbin_get():
    r = requests.get("https://www.baidu.com",headers={"accept": "application/json"})
    assert r.status_code ==200