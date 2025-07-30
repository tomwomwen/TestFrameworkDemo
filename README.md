# TestFrameworkDemo - Python自动化测试框架

## 项目简介

这是一个基于Python的Web自动化测试框架，采用POM（Page Object Model）设计模式，支持数据驱动测试，能够生成专业的HTML测试报告。

## 技术栈

- **测试框架**: Pytest
- **Web自动化**: Selenium WebDriver  
- **设计模式**: POM (Page Object Model)
- **数据驱动**: CSV + Faker
- **测试报告**: pytest-html + pytest-cov
- **API测试**: Requests
- **版本控制**: Git

## 项目结构

```
TestFrameworkDemo/
├── pages/                    # 页面对象层
│   ├── __init__.py
│   ├── base_page.py         # 基础页面类
│   └── baidu_page.py        # 百度页面类
├── tests/                   # 测试用例层
│   ├── __init__.py
│   ├── test_demo.py         # 基础测试
│   ├── test_web_ui.py       # Web UI测试
│   ├── test_api.py          # API测试
│   └── test_data_driven.py  # 数据驱动测试
├── utils/                   # 工具类
│   ├── __init__.py
│   ├── test_helpers.py      # 测试辅助工具
│   └── data_factory.py      # 测试数据工厂
├── data/                    # 测试数据
│   └── test_data.csv        # CSV测试数据
├── reports/                 # 测试报告
│   └── report.html          # HTML测试报告
├── requirements.txt         # 依赖文件
├── pytest.ini             # pytest配置
└── conftest.py            # pytest全局配置
```

## 快速开始

### 1. 环境准备
```bash
# 克隆项目
git clone [your-repo-url]
cd TestFrameworkDemo

# 安装依赖
pip install -r requirements.txt

# 下载ChromeDriver（确保版本匹配）
```

### 2. 运行测试
```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_web_ui.py

# 生成HTML报告
pytest --html=reports/report.html

# 生成覆盖率报告
pytest --cov=pages --cov=utils --cov-report=html
```

## 项目特色

### POM设计模式
- **BasePage**: 封装通用页面操作方法
- **具体页面类**: 继承BasePage，定义页面特有元素和操作
- **测试用例**: 调用页面类方法，保持简洁

### 数据驱动测试
- **数据工厂**: 动态生成测试数据
- **CSV文件**: 管理静态测试数据
- **参数化测试**: 支持批量测试执行

### 专业测试报告
- **HTML报告**: 可视化测试结果
- **覆盖率统计**: 代码覆盖情况分析
- **详细日志**: 完整的测试执行记录

## 测试用例说明

### Web UI测试
- 百度搜索功能测试
- 多关键词搜索验证
- 搜索结果页面检查

### API测试
- HTTP请求状态码验证
- JSON响应数据检查
- 接口异常处理测试

### 数据驱动测试
- CSV文件数据读取
- 参数化测试执行
- 批量数据验证

## 配置说明

### pytest.ini配置
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
log_cli = true
log_cli_level = INFO
```

### requirements.txt
```
pytest==8.4.1
pytest-html==4.1.1
pytest-cov==4.0.0
selenium==4.15.0
requests==2.31.0
faker==20.1.0
```

## 开发者说明

这个项目展示了：
- 标准的自动化测试框架设计
- POM设计模式的实际应用
- 数据驱动测试的实现方法
- 专业测试报告的生成

适合用于：
- Python自动化测试学习
- 企业级测试框架参考
- 面试项目展示

## 项目亮点

1. **设计模式**: 采用POM模式，代码维护性强
2. **数据驱动**: 支持CSV和动态数据生成
3. **报告完善**: HTML报告 + 覆盖率统计
4. **结构清晰**: 分层设计，职责明确
5. **易于扩展**: 新增页面和测试用例简单

## 使用场景

- **学习用途**: Python自动化测试入门项目
- **企业参考**: 测试框架设计规范示例
- **面试展示**: 完整的项目经验证明
- **扩展开发**: 可基于此框架开发更复杂功能

## 技术实现要点

### 页面对象模式实现
```python
# BasePage基础类设计
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
    
    def find_element(self, locator, timeout=10):
        # 元素定位方法
        pass
    
    def click(self, locator):
        # 点击操作
        pass
```

### 数据驱动测试实现
```python
# pytest参数化装饰器使用
@pytest.mark.parametrize("keyword,expected", [
    ("Python", "Python"),
    ("自动化测试", "自动化测试"),
    ("Selenium", "Selenium")
])
def test_search(keyword, expected):
    # 测试逻辑
    pass
```

### 测试报告配置
```python
# conftest.py配置示例
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
```

## 联系方式

如有问题，欢迎交流讨论！

---
**项目创建时间**: 2025年  
**技术水平**: 中级  
**适用场景**: Web自动化测试、学习项目、面试展示