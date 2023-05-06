import random

k = 36
maxlength = 16


def f(x, cnt):
    cnt += 1
    r = 2**k
    #print(x , cnt)
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
    minus = False
    if x < 0:
        minus = True
        x, cnt = g(-x)
    
    #print(x,cnt)
    sub = maxlength - digit(x)
    ret = x
    for i in range(sub - digit(cnt)):
        ret *= 10
        if minus:
            ret += pow(x % 10, x % 10 * i, 10)
        else:
            ret += pow(i % 10 - i % 2, i % 10 - i % 2 + 1, 10)
    #print(ret,cnt)
    ret += cnt * 10 ** (maxlength - digit(cnt))
    #print(ret,cnt)
    return ret


def int_generator(x):
    ret = -x
    x_, cnt = f(x, 0)
    while x_ > 0:
        ret = x_
        x_, cnt = f(x_, cnt)
    return pad(ret, cnt)


print("int_generator(num1):{}".format(int_generator(0)))
print("int_generator(num1):{}".format(int_generator(26476543)))
print("int_generator(num1):{}".format(int_generator(26476544)))

for i in range(2**(k-1)+1,20236000000,-1):
    num = int_generator(i)
    if num == 2264663430088446:
        print(i)
        break
    if num == 6772814078400884:
        print(i)
        break

    #print(f"{num}  {i}")
    if (i % (10 ** 6)) == 0:
        print("-----------")
        print(num)
        print(i)
        print("------------------")

#for i in range(142220000,2**(k-1),1000):
#    num = int_generator(i)
##    print(str(num) + " " +str(num)[2:8] + " " + str(i))
#    if num == 6772814078400884:
#        print(str(num) + " " +str(num)[:8] + " " + str(i))
#        break