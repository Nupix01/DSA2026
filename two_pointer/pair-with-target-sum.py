def pair_target(nums:list[int],target:int)->tuple[int,int]:
    left,right=0,len(nums)-1
    while left<right:
        s=nums[left]+nums[right]
        if s== target:
            return left+1,right+1 # 1 -base index
        if s<target:
            left+=1
        else:
            right-=1
