def sortedsquare(nums:list[int])->list[int]:
    n=len(nums)
    res=[0]*n
    left,right,pos=0,n-1,n-1
    while left<=right:
        if abs(nums[left])>abs(nums[right]):
            res[pos]=nums[left]*nums[left]
            left+=1
        else:
            res[pos]=nums[right]*nums[right]
            right-=1
        pos-=1
    return res

test=[-2,3,4,5,6]
resullt=sortedsquare(test)

print(resullt)
