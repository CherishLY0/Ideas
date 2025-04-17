"""
主程序入口
"""
import os
from dotenv import load_dotenv

def main():
    """
    主函数
    """
    # 加载环境变量
    load_dotenv()
    
    # 示例：获取环境变量
    debug_mode = os.getenv("DEBUG", "False").lower() == "true"
    
    if debug_mode:
        print("Debug mode is enabled")
    
    print("Hello, World!")

if __name__ == "__main__":
    main() 