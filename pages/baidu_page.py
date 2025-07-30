
from selenium.webdriver.common.by import By
from .base_page import BasePage


class BaiduPage(BasePage):
    """百度首页页面对象类"""

    def __init__(self, driver):
        """初始化百度页面"""
        super().__init__(driver)
        self.url = "https://baidu.com"

        self.search_box = (By.ID, "kw")
        self.search_button = (By.ID, "su")
        self.total_page = (By.ID, "ts")
        self.first_result = (By.CSS_SELECTOR,"h3 a")

    def open(self):
        self.driver.get(self.url)

    def search(self, keyword):
        self.input_text(self.search_box,keyword)
        self.click_element(self.search_button)

    def get_first_result(self):
        """获取第一个搜索结果的标题"""
        return self.get_text(self.first_result)
