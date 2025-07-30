# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """所有页面的基础类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self,locator):
        """找到页面元素"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self,locator):
        """点击页面元素"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self,locator,text):
        """向元素输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        """获取元素的文本内容"""
        element = self.find_element(locator)
        return element.text

    def is_element_present(self,locator,timeout=3):
        """检查元素是否存在（快速检查）"""
        try:
            # 用短时间等待找元素
            WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def take_screenshot(self, filename):
        """截取当前页面截图"""
        self.driver.save_screenshot(filename) # 用什么方法保存截图？
        return filename  # 返回文件名

    def get_page_title(self):
        """获取当前页面标题"""
        return self.driver.title

    def refresh_page(self):
        """刷新当前页面"""
        self.driver.refresh()