# TestFrameworkDemo - Python自动化测试框架

## 项目简介

基于Python开发的Web自动化测试框架，采用POM（Page Object Model）设计模式，支持数据驱动测试和代码覆盖率统计，能够生成专业的HTML测试报告。

## 技术栈

- **测试框架**: Pytest
- **Web自动化**: Selenium WebDriver
- **设计模式**: POM (Page Object Model)
- **数据驱动**: CSV文件 + Python数据工厂
- **测试报告**: pytest-html + pytest-cov
- **代码覆盖率**: Coverage.py
- **版本控制**: Git

## 项目结构

```
TestFrameworkDemo/
├── pages/                   # 页面对象层
│   ├── base_page.py        # 基础页面类
│   └── baidu_page.py       # 百度页面类
├── tests/                  # 测试用例层
│   ├── test_web_ui.py      # Web UI测试
│   ├── test_api.py         # API接口测试
│   ├── test_data_driven.py # 数据驱动测试
│   └── test_first.py       # 基础测试用例
├── data/                   # 测试数据
│   ├── data_factory.py     # 测试数据工厂
│   └── test_data.csv       # CSV测试数据
├── utils/                  # 工具类
├── config/                 # 配置文件
├── reports/                # 测试报告输出目录
├── .gitignore             # Git忽略文件配置
├── README.md              # 项目说明文档
├── requirements.txt       # Python依赖包
├── conftest.py           # Pytest全局配置
└── .coverage             # 代码覆盖率数据
```

## 环境准备

### 1. Python环境
- Python 3.7+
- pip包管理工具

### 2. 安装项目依赖
```bash
# 克隆项目
git clone https://github.com/tomwomwen/TestFrameworkDemo.git
cd TestFrameworkDemo

# 创建虚拟环境（推荐）
python -m venv .venv

# 激活虚拟环境
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 3. 浏览器驱动
- 下载对应版本的ChromeDriver
- 确保ChromeDriver在系统PATH中

## 使用方法

### 运行所有测试
```bash
pytest
```

### 运行指定测试文件
```bash
# 运行Web UI测试
pytest tests/test_web_ui.py

# 运行API测试
pytest tests/test_api.py

# 运行数据驱动测试
pytest tests/test_data_driven.py
```

### 生成测试报告
```bash
# 生成HTML测试报告
pytest --html=reports/report.html --self-contained-html

# 生成代码覆盖率报告
pytest --cov=pages --cov=utils --cov-report=html --cov-report=term
```

### 查看覆盖率数据
```bash
# 查看覆盖率统计
coverage report

# 生成HTML覆盖率报告
coverage html
```

## 框架特色

### POM设计模式
- **BasePage基础类**: 封装通用的页面操作方法
- **页面类继承**: 各页面类继承BasePage，实现页面特有功能
- **测试用例分离**: 测试逻辑与页面操作分离，提高可维护性

### 数据驱动测试
- **数据工厂模式**: 动态生成各种类型的测试数据
- **CSV数据管理**: 静态测试数据通过CSV文件管理
- **参数化测试**: 支持pytest.mark.parametrize批量测试

### 完善的测试报告
- **HTML可视化报告**: 清晰展示测试结果和失败详情
- **代码覆盖率统计**: 实时监控测试覆盖情况
- **详细执行日志**: 完整记录测试执行过程

## 测试用例类型

### Web UI自动化测试
- 页面元素定位和操作
- 表单填写和提交验证
- 页面跳转和内容检查
- 多浏览器兼容性测试

### API接口测试
- HTTP请求发送和响应验证
- JSON数据格式检查
- 接口状态码验证
- 异常情况处理测试

### 数据驱动测试
- 批量测试数据执行
- 边界值和异常数据测试
- 多场景参数化验证

## 配置文件说明

### pytest.ini
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short --strict-markers
log_cli = true
log_cli_level = INFO
```

### conftest.py
包含pytest全局配置和fixture定义

## 项目亮点

1. **标准POM架构**: 采用业界标准的页面对象模式
2. **完整测试覆盖**: Web UI + API + 数据驱动测试
3. **专业报告系统**: HTML报告 + 覆盖率统计
4. **模块化设计**: 清晰的分层架构，易于维护和扩展
5. **配置化管理**: 灵活的配置文件和环境管理
6. **版本控制集成**: 完善的Git配置和.gitignore规则

## 扩展开发

### 添加新的页面对象
1. 在`pages/`目录下创建新的页面类
2. 继承`BasePage`基础类
3. 定义页面特有的元素定位和操作方法

### 添加新的测试用例
1. 在`tests/`目录下创建测试文件
2. 导入对应的页面对象类
3. 编写测试方法，调用页面对象的方法

### 扩展数据工厂
1. 在`data/data_factory.py`中添加新的数据生成方法
2. 支持更多类型的测试数据生成

## 最佳实践

- 保持页面对象类的简洁，只包含页面相关的操作
- 测试用例应该独立，不依赖其他测试的执行结果
- 使用有意义的断言消息，便于问题定位
- 定期更新依赖包版本，确保安全性
- 遵循Python PEP8编码规范