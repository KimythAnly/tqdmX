import time
import random
from tqdmX import TqdmWrapper, format_str


form = \
'This is a template\n\
# var1:{var1}\n\
# var2:{var2}\n\
# var3:{var3}'



for ep in range(10):
    tw = TqdmWrapper(range(5), desc=f'T{ep}')
    tw.set_ctrls('key', 'red')
    for i in tw:
        var4 = random.random()
        var5 = random.random()
        tw.add(form.format(var1=i, var2='back'*(10-i), var3='adsfsafd'))
        tw.add([format_str('red', 'var4: '), format_str('white', f'var4')])
        tw.add({'var5': var5, 'var6': random.random()})
        tw.add({'var7': 1231, 'var8': 'hi'*i}, kv_format=format_str(['bold', 'red'], '{key} - ') + '{value}')
        tw.update()
        time.sleep(.2)
print('done')

