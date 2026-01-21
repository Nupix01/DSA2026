def movezero(nums:list[int]):
    write=0
    for read in range(len(nums)):
        if nums[read]!=0:
            nums[write],nums[read]=nums[read],nums[write]
            write +=1
    return nums

test=[1,0,0,2,0,0,1]
result=movezero(test)
print(result)