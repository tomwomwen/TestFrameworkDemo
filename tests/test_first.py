# 文件: tests/test_first.py
from selenium.webdriver.common.by import By
import time

def test_open_baidu(driver):  # 注意：参数名driver对应conftest.py中的函数名
    """测试：打开百度首页"""
    # 1. 打开百度网站
    driver.get("https://www.baidu.com/")
    # 2. 获取页面标题
    title = driver.title
    # 3. 验证标题包含"百度"
    assert "百度" in title


def test_search_python(driver):
    """测试：搜索Python"""
    # 1. 打开百度网站
    driver.get("https://www.baidu.com/")
    # 2. 找到搜索框，输入"Python"
    driver.find_element(By.ID, "kw").send_keys("python")
    # 3. 点击搜索按钮
    driver.find_element(By.ID, "su").click()
    # 4. 验证搜索结果
    time.sleep(2)
    title = driver.title
    assert "python" in title.lower()
