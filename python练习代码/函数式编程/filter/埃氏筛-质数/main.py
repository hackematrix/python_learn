"""埃氏筛质数"""       

# 生成奇序列
def _init_odd():
    n=1
    while True:
        n=n+2
        yield n

# 筛合数
def _not_divisible(n):
    return lambda x:n%x>0
    
#埃氏筛
def primes():
    yield 2
    it=_init_odd()

    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

for i in primes():
    if i<20:
        print(i)
    else:
        break    
