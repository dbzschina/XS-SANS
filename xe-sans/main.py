#  if __name__ == '__main__':
import gonen
import time

op = False

sr=input('按任意键继续...')
if sr == 'su':
    op = True
else:
    time.sleep(1)
if not op:
    print('xe-sans 1.0')
    print('如有疑问，请输入\'help\'')
else:
    print('xe-sans 1.0 管理员')
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
    elif sr == 'us':
        if not op:
            time.sleep(0.5)
        else:
            var = op = False
    elif sr == 'quit':
        break
    elif sr == '':
        time.sleep(0.1)
    else:
        print(f'错误的{sr}')

