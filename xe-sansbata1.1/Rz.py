import subprocess
import sys
from datetime import datetime

version = "xe-sans bata 1.1"#   版本号

class LogMonitor:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.proc = None
        self.active = False

    def start(self):
        if self.active:
            return True

        display_code = """
import sys
import io
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

print("=" * 50)
print("日志监测")
print("=" * 50)
print()
print("等待日志...")
print("-" * 50)
sys.stdout.flush()

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
        if line.strip():
            print(line.strip())
            sys.stdout.flush()
    except:
        break

print()
print("=" * 50)
print("  监听已停止")
print("=" * 50)
input("按回车键退出...")
"""

        try:
            self.proc = subprocess.Popen(
                [sys.executable, "-c", display_code],
                stdin=subprocess.PIPE,
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            self.active = True
            return True
        except Exception as e:
            print(f"启动失败: {e}")
            return False

    def log(self, level, message):
        if not self.active or not self.proc:
            return
        try:
            now = datetime.now()
            log_entry = f"{version} | {now.year} {now.month} {now.day} | {level} | {message}"
            self.proc.stdin.write((log_entry + "\n").encode('utf-8'))
            self.proc.stdin.flush()
        except Exception as e:
            print(f"写日志失败: {e}")
            self.active = False

    def info(self, message):
        self.log("INFO", message)

    def warning(self, message):
        self.log("WARNING", message)

    def error(self, message):
        self.log("ERROR", message)

    def stop(self):
        if self.proc:
            try:
                self.proc.stdin.close()
            except:
                pass
            self.active = False

    def is_active(self):
        return self.active

monitor = LogMonitor()

if __name__ == "__main__":
    print("启动日志监测...")
    if monitor.start():
        print("窗口已打开，正在发送测试日志...")
        monitor.info("测试日志 1")
        monitor.info("测试日志 2")
        monitor.warning("测试警告")
        monitor.error("测试错误")
        print("日志已发送，请在弹出的窗口中查看")
        input("按回车键关闭...")
        monitor.stop()
    else:
        print("启动失败")
