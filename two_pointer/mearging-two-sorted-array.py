def mergeArray(num1:list[int],num2:list[int],m,n)->list[int]:
    i,j,k = m-1,n-1,m+n-1
    while j>0:
        if i>=0 and num[i]>num[j]:
            num1[k]=num1[i]
            j-=1
        else :
            num1[k]=num2[j]
            i-=1
    return num1
