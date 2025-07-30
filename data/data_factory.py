import random
from faker import Faker
from  datetime import datetime,timedelta


class TestDataFactory:
    """测试数据工厂类 - 生成各种测试数据"""

    def __init__(self):
        """初始化数据工厂"""
        self.fake = Faker('zh_CN')  # 使用中文数据
    def generate_user_data(self, count=1):
        """生成用户测试数据"""
        #步骤：创建一个空列表存储用户数据
        users = []
        for i in range(count):
            user = {
                "username":self.fake.user_name(),
                "name": self.fake.name(),
                "email": self.fake.email(),
                "phone": self.fake.phone_number(),
                "address": self.fake.address(),
            }
            # 步骤4：把这个用户添加到列表中
            users.append(user)

        # 步骤5：根据count决定返回什么
        if count == 1:
            return users[0]
        else:
            return users
    def generate_search_keywords(self,count=1):
        """生成搜索关键词数据"""
        # 步骤1：预定义各种类型的关键词
        programming_keywords = ["Python", "Java", "C++", "JavaScript", "HTML"]
        tech_keywords = ["人工智能", "大数据", "云计算", "区块链"]
        city_keywords = ["北京", "上海", "广州", "深圳"]

        all_keywords = programming_keywords + tech_keywords + city_keywords

        selected_keywords = []
        for i in range(count):
            random_keyword = random.choice(all_keywords)
            selected_keywords.append(random_keyword)

        if count == 1:
            return selected_keywords[0]
        else:
            return selected_keywords

    def generate_boundary_test_data(self, data_type="string"):
        """生成边界值测试数据"""
        # 根据data_type生成不同类型的边界值
        # string: 空字符串、长字符串、特殊字符
        # number: 0, -1, 最大值、最小值
        # 返回边界值列表

        if data_type == "string":
            return [
                "",
                "a",
                "fadsfdfiangidnagi",
                "!@$@$@$(*&"
            ]
        elif data_type == "number":
            return [
                0,
                -1,
                1,
                334324234,
            ]
        else:
            return ["","test"]

    def generate_test_config(self, config_type="browser"):
        """生成测试配置数据"""

        if config_type == "browser":
            # 浏览器配置选项
            browsers = ["Chrome", "Firefox", "Edge"]
            sizes = ["大窗口", "中窗口", "小窗口"]

            selected_browser = random.choice(browsers)
            selected_size = random.choice(sizes)

            return {
                "browser": selected_browser,
                "size": selected_size,
                "timeout": 10
            }

        else :
            return {"browser": "Chrome", "timeout": 10}