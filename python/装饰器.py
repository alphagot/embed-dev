# __author:  xiaoxinpro13
# date:  2020/8/15
import time


def foo():
    time.sleep(1)
    print('foo')


def logit(fn):
    def inner():
        print('---')
        fn()
        print('***')
    return inner


foo = logit(foo)

foo()


#语法糖

@logit
def mark():
    time.sleep(2)
    print('mark')

mark()