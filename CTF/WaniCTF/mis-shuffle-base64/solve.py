for list in shuffle_list:
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