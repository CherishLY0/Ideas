# Python Project Template

这是一个可扩展的Python项目模板，提供了基本的项目结构和开发工具配置。

## 项目结构

```
project/
├── src/                    # 源代码目录
│   ├── __init__.py
│   └── main.py            # 主程序入口
├── tests/                 # 测试目录
│   ├── __init__.py
│   └── test_main.py
├── .env                   # 环境变量文件
├── .gitignore            # Git忽略文件
├── requirements.txt      # 项目依赖
└── README.md            # 项目说明文档
```

## 安装

1. 克隆项目：
```bash
git clone [项目地址]
cd [项目目录]
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 开发

- 运行测试：
```bash
pytest
```

- 代码格式化：
```bash
black .
```

- 代码检查：
```bash
flake8
```

## 项目特点

- 模块化设计
- 完整的测试框架
- 代码质量工具集成
- 环境变量管理
- 清晰的文档结构