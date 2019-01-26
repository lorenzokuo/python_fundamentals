def selectSort(arr):
    min = arr[0]
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < min:
            	min = arr[j]
            	arr[i],arr[j] = arr[i],arr[j]
	print (arr) 

selectSort([5,2,1,3,8])