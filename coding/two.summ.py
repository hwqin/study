def two_sum_pairs(arr, target):
    num_count = {}
    result = []

    for num in arr:
        complement = target - num
        if num_count.get(complement, 0) > 0:
            result.append([complement, num])
            num_count[complement] -= 1  # Use up the complement
        else:
            num_count[num] = num_count.get(num, 0) + 1

    return result

##
## check delta value (target-num), if in dict then pair it, reduce the value in dict by 1
## if not in dict, then add num to dict (value + 1) as there might be dup elements
##

