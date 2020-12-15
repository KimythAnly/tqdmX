import time
import random
from tqdmX import TqdmWrapper, format_str


form = \
'This is a template\n\
# var1:{var1}\n\
# var2:{var2}\n\
# var3:{var3}'

tw = TqdmWrapper(range(20), desc=f'T1')
tw.set_ctrls('key', 'red')

for i in tw:
    var4 = random.random()
    var5 = random.random()
    tw.add(form.format(var1=i, var2='back'*(10-i), var3='adsfsafd'))
    tw.add([format_str('blue', 'var4: '), format_str('white', f'var4')])
    tw.add({'var5': var5})
    tw.update()
    time.sleep(0.1)

print('done')

