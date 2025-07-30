import requests
import time

def test_baidu_homepage_status():
    response = requests.get("https://www.baidu.com")

    assert response.status_code == 200

    print(f"状态码：{response.status_code}")

def test_baidu_response_time():
    response = requests.get("https://www.baidu.com")
    total_seconds = response.elapsed.total_seconds()
    assert total_seconds < 3

