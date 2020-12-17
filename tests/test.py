import time
import random
from tqdmX import TqdmWrapper, format_str


form = \
'This is a template\n\
var1: {var1:0>4}\n\
var2: {var2}\n\
Time elapsed: {var3:.3f} (sec)'

start = time.time()

for ep in range(2):
    tw = TqdmWrapper(range(10), desc=f'T{ep}')
    tw.set_ctrls('key', 'red')
    for i in tw:
        var4 = random.random()
        var5 = random.random()
        time_elapsed = (time.time() - start)
        tw.add(form.format(var1=i, var2='back'*(10-i), var3=time_elapsed))
        tw.add([format_str('red', 'var4: '), format_str('white', f'var4')])
        tw.add({'var5': var5, 'var6': random.random()})
        tw.add({'var7': 1231, 'var8': 'hi'*i}, kv_format=format_str(['bold', 'red'], '{key} - ') + '{value}')
        tw.update()
        time.sleep(.2)
print('done')

