import sys
import shutil
import re
import time
from addict import Dict
from tqdm import tqdm

symbols = Dict({
        'prev_line': '\033[F',
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'yellow': '\033[93m',
        'magenta': '\033[95m',
        'grey' : '\033[90m',
        'black' : '\033[90m',
        'default' : '\033[99m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    })


def format_str(fmt, s, end=None):
    if end is None:
        end = symbols.end
    if isinstance(fmt, list):
        return ''.join([symbols[f] for f in fmt]) + str(s) + end
    return symbols[fmt] + str(s) + end

# =========================================================
#  Source: https://stackoverflow.com/questions/2186919
#  Author: John Machin
# =========================================================
strip_ANSI_escape_sequences_sub = re.compile(r"""
    \x1b     # literal ESC
    \[       # literal [
    [;\d]*   # zero or more digits or semicolons
    [A-Za-z] # a letter
    """, re.VERBOSE).sub
def strip_ANSI_escape_sequences(s):
    return strip_ANSI_escape_sequences_sub("", s)
# =========================================================

class TqdmWrapper():
    def __init__(self, iterable, depth=0, **kwargs):
        self.fp = sys.stdout
        self.tqdm = tqdm(iterable, dynamic_ncols=True, **kwargs)
        self.depth = depth
        self.msg = ''
        self._msg = ''
        self.default_kv_format = format_str(['bold', 'blue'], '{key}: ') + '{value}'
        self.ctrls = Dict({
            'default': 'default',
            'end': 'end'
        })

    def set_ctrls_by_dict(self, dct):
        for k, v in dct.items():
            self.set_ctrls(k, v)

    def set_ctrls(self, k, v):
        self.ctrls[k] = v

    def __iter__(self):
        for i in self.tqdm:
            yield i

    def _add_str(self, msg):
        return msg

    def _add_list(self, msg):
        return ''.join(msg)

    def _add_dict(self, msg, kv_format):
        if kv_format is None:
            kv_format = self.default_kv_format
        ret = '\n'.join([kv_format.format(key=k, value=v)
         for k, v in msg.items()])
        return ret

    def add(self, msg, kv_format=None):
        if isinstance(msg, str):
            _msg = self._add_str(msg)
        elif isinstance(msg, list):
            _msg = self._add_list(msg)
        elif isinstance(msg, dict):
            _msg = self._add_dict(msg, kv_format)
        if len(self.msg) > 0:
            self.msg = self.msg + '\n' + _msg
        else:
            self.msg = _msg

    def fill(self, msg):
        maxcols = shutil.get_terminal_size()[0]
        # return f'{msg:<{maxcols}}'
        exp = maxcols - len(strip_ANSI_escape_sequences(msg))
        return f'{msg}{" "*exp}'

    def update(self, *args):
        if len(self._msg) > 0:
            n_line = self._msg.count('\n') +1
        else:
            n_line = 0
        _msg_filled = [self.fill(m) for m in self.msg.split('\n')]
        _msg = '\n'.join(_msg_filled)
        self._msg = n_line * symbols.prev_line + _msg
        tqdm.write(self._msg, self.fp)
        self.msg = ''

__all__ = [
    'TqdmWrapper',
    'format_str'
]
