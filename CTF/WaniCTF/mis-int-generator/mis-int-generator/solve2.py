import random

k = 36
maxlength = 16


def f(x, cnt):
    cnt += 1
    r = 2**k
    if x == 0 or x == r:
        return -x, cnt
    if x * x % r != 0:
        return -x, cnt
    else:
        return -x * (x - r) // r, cnt


def g(x):
    ret = x * 2 + x // 3 * 10 - x // 5 * 10 + x // 7 * 10
    ret = ret - ret % 2 + 1
    return ret, x // 100 % 100


def digit(x):
    cnt = 0
    while x > 0:
        cnt += 1
        x //= 10
    return cnt


def pad(x, cnt):
    print("before_pad:{} cnt:{}".format(x,cnt))
    minus = False
    if x < 0:
        minus = True
        x, cnt = g(-x)
    sub = maxlength - digit(x)
    ret = x
    for i in range(sub - digit(cnt)):
        ret *= 10
        if minus:
            ret += pow(x % 10, x % 10 * i, 10)
        else:
            ret += pow(i % 10 - i % 2, i % 10 - i % 2 + 1, 10)
    ret += cnt * 10 ** (maxlength - digit(cnt))
    print("after_pad:{} cnt:{}".format(ret,cnt))
    return ret


def int_generator(x):
    ret = -x
    x_, cnt = f(x, 0)
    while x_ > 0:
        ret = x_
        x_, cnt = f(x_, cnt)
    #print("beforePad{}".format(ret))
    return pad(ret, cnt)

def inv_int_generator(x):
    ret = unpad(x)
    #print("inv_before_pad{}".format(ret))
    x_, cnt = inv_f(ret, 0)
    while x_ < 0:
        ret = x_
        x_, cnt = f(x_, cnt)
    
    return x_


def inv_f(x,cnt):
    cnt -= 1
    r = 2**k

    x_ = -x

    if x_ == 0 or x_ == r:
        return -x, cnt
    if x_ * x_ % r != 0:
        return -x, cnt
    else:
        return -x // (x - r) * r, cnt

def unpad(ret):
    print("before_unpad:{}".format(ret))
    cnt = int(str(ret)[:2])
    print("cnt:{}".format(cnt))

    minus = True
    ret -= cnt * 10 ** (maxlength - digit(cnt))

    sub = maxlength - digit(ret) - digit(cnt)
    for i in range(sub):
        if minus:
            ret -= pow(ret % 10, ret % 10 * i, 10)
        else:
            ret -= pow(i % 10 - i % 2, i % 10 - i % 2 + 1, 10)
        ret /= 10
    
    x = ret
    if (minus):
        x = inv_g(-x)

    #x = x
    print("after_unpad:{}".format(x))
    return -x 

def inv_g(x):
    if x %2 == 0:
        x += 1
    else:
        x += 2
    
    return x*21//100


num1 = 1008844668800884
num2 = 2264663430088446
num3 = 6772814078400884

inv1 = inv_int_generator(num1)
inv2 = inv_int_generator(num2)
inv3 = inv_int_generator(num3)
print("original:{}".format(inv1))
print("original:{}".format(inv2//100))
print("original:{}".format(inv3//100))