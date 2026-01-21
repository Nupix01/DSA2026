def mergeArray(num1:list[int],num2:list[int],m,n)->list[int]:
    i,j,k = m-1,n-1,m+n-1
    while j>=0:
        if i>=0 and num1[i]>num2[j]:
            num1[k]=num1[i]
            i-=1
        else :
            num1[k]=num2[j]
            j-=1
    k-=1
