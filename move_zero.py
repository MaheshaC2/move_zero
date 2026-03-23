#moves all the zeros to end
def move_zeros(nums):
    result = []
    zeros = 0
    
    for num in nums:
        if num == 0:
            zeros += 1
        else:
            result.append(num)
    
    return result + [0] * zeros
