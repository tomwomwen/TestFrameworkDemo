import pytest
import pandas as pd
from pages.baidu_page import BaiduPage
import time


@pytest.fixture(scope="module")
def test_data():
    """读取CSV测试数据"""
    df = pd.read_csv("./data/test_data.csv")  # ← 确保文件名正确

    test_params = []
    for row in df.itertuples():
        test_params.append((row[1], row[2], row[3]))
    return test_params


@pytest.mark.parametrize("keyword,expected,test_type",
                         [("Python", "Python", "programming"),
                          ("Java", "Java", "programming")])  # 先用固定数据测试
def test_baidu_search_parametrize(driver, keyword, expected, test_type):
    """参数化搜索测试"""
    # 创建百度页面对象
    baidu_page = BaiduPage(driver)

    # 打开百度首页
    baidu_page.open()

    # 搜索关键词
    baidu_page.search(keyword)

    # 等待结果加载
    time.sleep(2)

    # 验证搜索结果
    result = baidu_page.get_first_result()
    assert expected.lower() in result.lower()

    print(f"✅ 搜索 '{keyword}' 成功，类型：{test_type}")

def test_baidu_search_csv(driver,test_data):
    for data in test_data:
        keyword = data[0]
        expected = data[1]
        test_type = data[2]

        # 创建百度页面对象
        baidu_page = BaiduPage(driver)

        # 打开百度首页
        baidu_page.open()

        # 搜索关键词
        baidu_page.search(keyword)

        # 等待结果加载
        time.sleep(2)

        # 验证搜索结果
        result = baidu_page.get_first_result()
        assert expected.lower() in result.lower()

        print(f"✅ 搜索 '{keyword}' 成功，类型：{test_type}")