"""
time_random随机数生成器，基于时间的随机数生成器  

time_random包含下列随机数生成器：  
`TimeRandom`  
- 通过将时间作为随机源生成随机数，再将生成的随机数与一个由random库生成的随机数进行运算得到随机数  
- 可以提供其他的随机源，把随机数生成器类传入Random参数即可  

`TimeRandomOrigin`  
- 通过将时间作为随机源生成随机数，没有经过其他的加工  
"""

from random import Random
from time import perf_counter
from struct import pack

BPF = 53
RECIP_BPF = 2 ** -BPF
MAX_INT = (1 << 53) - 1

def _reduce_bytes(byte: bytes, length: int):
    if len(byte) < length:
        raise ValueError('提供的字节长度必须大于或等于目标长度')
    if len(byte) == length:
        return byte
    while len(byte) > length:
        tmp_array = bytearray()
        for i in range(0, len(byte) - 1):
            tmp_array.append(byte[i] ^ byte[i + 1])
        byte = bytes(tmp_array)
    return byte

class TimeRandomOrigin(Random):
    def random(self):
        return (int.from_bytes(_reduce_bytes(pack('d', perf_counter()), 7))
               >> 3) * RECIP_BPF

class TimeRandom(Random):
    def __init__(self, Random: type[Random] = Random):
        self._rinst = Random()
        self._rrandom = self._rinst.random
        self._tinst = TimeRandomOrigin()
        self._trandom = self._tinst.random
    
    def random(self):
        r = int(self._rrandom() * MAX_INT)
        t = int(self._trandom() * MAX_INT)
        return ((r ^ t) & MAX_INT) * RECIP_BPF