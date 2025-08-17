# time_random_generator
使用时间作为随机源的随机数生成器

本项目包含下列程序：  
- `time_random.py`  
- `test.py`  

---

## `time_random.py`  
项目的主要部分  

程序中包含两个类：  
- `TimeRandom`  
- `TimeRandomOrigin`  
它们都继承了`random.Random`。  

### `TimeRandom`
使用`TimeRandomOrigin`产生随机数后，再将其与一个由`random`库产生的随机数进行一定运算，在一定程度上避免了可能的因为时间重复导致的产出随机数重复的问题。  
由于经过了额外的计算，产出随机数可能花费较长时间。  

### `TimeRandomOrigin`  
使用`time.perf_counter`作为随机源。  
可能由于时间的重复导致产出的随机数相同。  

---

## `test.py`  
测试程序  

会按照下列顺序测试：  
1. `random.Random`  
2. `time_random.TimeRandomOrigin`  
3. `time_random.TimeRandom`  

对每个类进行`1_000_000`次测试，并计算其平均值、花费时间。  

