"""
主程序测试
"""
import os
from src.main import main

def test_main(capsys):
    """
    测试主函数
    """
    # 设置环境变量
    os.environ["DEBUG"] = "true"
    
    # 运行主函数
    main()
    
    # 捕获输出
    captured = capsys.readouterr()
    
    # 验证输出
    assert "Debug mode is enabled" in captured.out
    assert "Hello, World!" in captured.out 