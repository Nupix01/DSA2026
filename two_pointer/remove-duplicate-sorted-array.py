def remove_dupe(nums:list[int])->int:
    if not nums:
        return 0
    write=1
    for read in range (1,len(nums)):
        if nums[read] !=nums[write-1]:
            num[write]=num[read]
            write+=1
    return write
