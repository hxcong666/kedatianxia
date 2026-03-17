# 客达天下 API 自动化测试框架

这是一个基于 Python + Pytest + Requests + Allure 的接口自动化测试项目，主要针对“客达天下”系统进行测试。

## 📁 目录结构

- `api/`: 接口封装层，定义了各个模块的 API 请求方法（如登录、课程管理、合同管理）。
- `script/`: 测试脚本层，存放具体的测试用例（如 `ContractTest.py`）。
- `data/`: 测试数据层，存放测试所需的 JSON 或文本数据。
- `report/`: 测试报告层，存放 Pytest 生成的测试结果和 Allure 报告数据。
- `common/`: 公共方法层。
- `config.py`: 项目配置文件，包含基础 URL 等配置。
- `pytest.ini`: Pytest 运行配置文件。

## 🛠️ 技术栈

- **Python**: 编程语言
- **Pytest**: 测试框架
- **Requests**: HTTP 请求库
- **Allure**: 测试报告生成工具

## 🚀 快速开始

### 1. 环境准备

确保已安装 Python 环境，并安装以下依赖库：

```bash
pip install pytest requests allure-pytest
```

**注意**: 需要先安装 Allure 命令行工具才能生成和查看可视化报告。

### 2. 配置

在 `config.py` 中配置系统的基础 URL：

```python
BASE_URL = "http://kdtx-test.itheima.net"
```

### 3. 运行测试

在项目根目录下运行以下命令执行测试：

```bash
pytest
```

或者运行指定的测试文件：

```bash
pytest script/ContractTest.py
```

测试结果数据将生成在 `report/` 目录下。

### 4. 查看测试报告

测试完成后，使用 Allure 查看可视化报告：

```bash
allure serve report
```

## 📝 测试模块

目前包含以下测试模块：

- **登录 (Login)**: 验证用户登录功能 (包含验证码获取)。
- **课程管理 (Course)**: 验证添加课程等功能。
- **合同管理 (Contract)**: 验证合同上传等功能。

## 📄 其它说明

- `pytest.ini` 文件中配置了默认的运行参数（如 `-s` 输出控制台信息，`--alluredir report` 生成报告数据）。
- 测试用例采用了 setup/teardown 模式进行初始化和清理。
- 数据驱动测试使用 `data/` 目录下的 JSON 文件（如 `login.json`）。
