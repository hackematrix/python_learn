"""判断是否是奇数"""
def is_odd(n):
    return n%2==1

list_1=list(filter(is_odd,[1,2,4,6,9,10,15]))

print(list_1)
