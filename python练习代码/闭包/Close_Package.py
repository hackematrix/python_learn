def lazy_num(*args):
    def sum():
        ax=0
        for _ in args:
            ax+=_
        return ax
    return sum

f=lazy_num(1,3,5,7,9)
test=f()
print(test)
