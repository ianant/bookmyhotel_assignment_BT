def find_subarrays(arr):
    length=len(arr)
    listOfSubArrays=[]

    j=0
    for i in range(length-2):
        oddnum = 0
        j = i
        while oddnum != 3:
            if arr[j]%2==0:
                j+=1
            else:
                oddnum+=1
                j+=1
            if(oddnum==3):
                listOfSubArrays.append(arr[i:j])
        if i > length-3:
            break

    return listOfSubArrays

arr = [1,2,1,2,1,1,5]
result = find_subarrays(arr)
print("Subarrays :")
for subarrays in result:
    print(subarrays)

