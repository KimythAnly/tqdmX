# tqdmX
This is a tqdm wrapper for multi-line logging.

## Demo
<img src="/demo.gif" width="768"/>

## Requirements
- tqdm
- addict

You can install the requirements using the following script.
```
pip install -r requirements.txt
```

## Usage
The following is a simple example.
```python
import time
from tqdmX import TqdmWrapper, format_str
tw = TqdmWrapper(range(10))
for i in tw:
  tw.add(f'Iter {i}')
  tw.add('line1')
  tw.add(format_str('blue','line2'))
  tw.update()
  time.sleep(0.5)
```

For the demo gif shown above, you may refer to `test.py`.
