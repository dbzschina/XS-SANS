import gonen
import time
import importlib.util
import os

log_module_path = os.path.join(os.path.dirname(__file__), 'Rz.py')
spec = importlib.util.spec_from_file_location("Rz", log_module_path)
log_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(log_module)

op = False
log_monitor = log_module.monitor

sr=input('按任意键继续...')
if sr == 'su':
    op = True
else:
    time.sleep(1)
if not op:
    print('xe-sans bata 1.1')
    print('如有疑问，请输入\'help\'')
else:
    print('xe-sans bata 1.1 管理员')
    print('如有疑问，请输入\'help\'')

while True:
    if not op:
        sr=input('>>')
    else:
        sr=input('$>>')
    if sr == 'help':
        if not op:
            gonen.helph()
        else:
            gonen.help()
    elif sr == 'calc':
        sza = input('数字一:')
        szb = input('数字二:')
        zf = input('符号:')
        sc = gonen.calac(sza, szb, zf)
        print(f'结果:{sc}')
        if log_monitor.is_active():
            log_monitor.info(f'计算器: {sza} {zf} {szb} = {sc}')
    elif sr == 'us':
        if not op:
            time.sleep(0.5)
        else:
            var = op = False
    elif sr == 'log':
        if log_monitor.is_active():
            print('日志监测已在运行')
        else:
            if log_monitor.start():
                print('日志监测已启动')
                log_monitor.info('日志系统已就绪')
            else:
                print('日志监测启动失败')
    elif sr == 'quit':
        if log_monitor.is_active():
            log_monitor.info('程序退出')
            log_monitor.stop()
        break
    elif sr == '':
        time.sleep(0.1)
    else:
        print(f'错误的{sr}')
        if log_monitor.is_active():
            log_monitor.warning(f'用户输入了无效命令: {sr}')
