def reverse_string(input:list[str])->None:
    left,right=0,len(input)-1 # assing o to left and input lenth to right
    while left<right:
        input[left],input[right]=input[right],input[left]
        left+=1
        right-=1

s = ["h","e","l","l","o"]

reverse_string(s)
print(s)


