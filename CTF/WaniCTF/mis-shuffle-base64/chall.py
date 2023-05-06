import random
import itertools
import base64
import hashlib


def make_shuffle_list(m):
    num = []
    for i in range(len(m) // 3):
        num.append(i)

    print(num)

    return list(itertools.permutations(num, len(m) // 3))


def make_str_blocks(m):
    tmp = ""
    ret = []
    for i in range(len(m)):
        tmp += m[i]
        if i % 3 == 2:
            ret.append(tmp)
            tmp = ""
    return ret


def pad(m):
    ret = ""
    for i in range(len(m)):
        ret += m[i]
        if i % 2:
            ret += chr(random.randrange(33, 126))
    
    print(ret)

    while len(ret) % 3:
        ret += chr(random.randrange(33, 126))

    print(ret) 
    # 27 文字だと都合がいい

    return ret


flag = "FAKE{DUMMY_FLAGG}"
# FLAG check
# assert (hashlib.sha256(flag.encode()).hexdigest() == "19b0e576b3457edfd86be9087b5880b6d6fac8c40ebd3d1f57ca86130b230222")

padflag = pad(flag)
print("----------")
shuffle_list = make_shuffle_list(padflag)
#print(shuffle_list)
print("----------")
str_blocks = make_str_blocks(padflag)
print(str_blocks)
order = random.randrange(0, len(shuffle_list) - 1)
cipher = ""
for i in shuffle_list[order]:
    cipher += str_blocks[i]
print(cipher)
cipher = b'fWQobGVxRkxUZmZ8NjQsaHUhe3NAQUch'

print(f"cipher = {cipher}")

decoded_cipher = base64.b64decode(cipher).decode()
reversed_str_blocks = make_str_blocks(decoded_cipher)
print(reversed_str_blocks)


for list in make_shuffle_list(decoded_cipher):
    first_reversed_str = ""
    for i in list:
        first_reversed_str += reversed_str_blocks[i]
    
    second_reversed_strs = [first_reversed_str,first_reversed_str[:-1],first_reversed_str[:-2]]

    for str in second_reversed_strs:
        third_reversed_str = ""
        for j in range(len(str)):
            if j == 0:
                third_reversed_str += str[0]
            elif j % 3 != 2:
                third_reversed_str += str[j]
        
        if (hashlib.sha256(third_reversed_str.encode()).hexdigest() == "19b0e576b3457edfd86be9087b5880b6d6fac8c40ebd3d1f57ca86130b230222"):
            print(third_reversed_str)
            break

