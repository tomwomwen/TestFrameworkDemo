from pages.baidu_page  import BaiduPage
import time

def test_baidu_search_python(driver):
    """测试百度搜索Python功能"""
    baidu_page = BaiduPage(driver)
    baidu_page.open()
    baidu_page.search("Python")
    time.sleep(2)
    text = baidu_page.get_first_result()
    assert "python" in text.lower()

