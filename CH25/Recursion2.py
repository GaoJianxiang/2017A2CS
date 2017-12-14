#recursion2

def groupSum(start,nums,target):
    if target==0:
        return True
    if start == len(nums):
        return False
    return groupSum(start+1,nums,target-nums[start]) or groupSum(start+1,nums,target)
print(groupSum(0,[1,4,5],9))

def groupSum6(start,nums,target):
    if target == 0:
        return True
    if start == len(nums):
        return False
    if nums[start] == 6:
        return groupSum6(start+1,nums,target-nums[start])
    return groupSum6(start+1,nums,target-nums[start]) or groupSum6(start+1,nums,target)
print(groupSum6(0,[1,6,2],3))

def groupNoAdj(start,nums,target):
    if target==0:
        return True
    if start == len(nums) or start == len(nums)+1:
        return False
    return groupNoAdj(start+2,nums,target-nums[start]) or groupNoAdj(start+1,nums,target)
print(groupNoAdj(0,[1,4,5,7],9))

def groupSum5(start,nums,target):
    if target==0:
        return True
    if start == len(nums):
        return False
    if nums[start]%5 ==0:
        if nums[start+1]==1:
            return groupSum5(start+2,nums,target-nums[start])
        else:
            return groupSum5(start+1,nums,target-nums[start]) 
    return groupSum5(start+1,nums,target-nums[start])or groupSum5(start+1,nums,target)
print(groupSum5(0,[2,5,10,1],16))

def groupSumClump(start,nums,target):
    if target==0:
        return True
    if start >= len(nums):
        return False
    count =1
    while nums[start]==nums[start+1]:
        count=count+1
        start+=1
    return groupSumClump(start+count,nums,target-nums[start]*count) or groupSumClump(start+count,nums,target)
print(groupSumClump(0,[1,3,3,3,2],7))

def splitArray(nums,target=0,start=0):
    if target == sum(nums)/2:
        return True
    if start >=len(nums):
        return False
    return splitArray(nums,target=target+nums[start],start= start+1)or splitArray(nums,target=target,start=start+1)
print (splitArray([2,5,3]))

def splitOdd10(nums,target=0,start=0)

