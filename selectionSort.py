arr = [2,4,6,7,3,9,5,8,1,]

def selectSort(arr):
	for j in range(len(arr)-1):
		print("\n\n","-"*50, "Iteration", j)
		index=j
		for i in range(1+j,len(arr)):
			print("\n","*"*80,"\ncomparing", arr[j],arr[i])
			print("i = ", i)
			if arr[i]<arr[index]:
				index=i
				print("min =",arr[index])
			else:
				print("no need to swap", arr[j], arr[i])
		arr[j],arr[index] = arr[index],arr[j]
		print("swapped!", arr[j],arr[i])
		print("array is now",arr)
	return arr

print(selectSort(arr))


# simplify
# for i in range(len(arr)):
# 	min_idx = i
# 	for j in range(i+1, len(arr)):
# 		if arr[min_idx]>arr[j]:
# 			min_idx = j
# 	arr[i],arr[min_idx]=arr[min_idx],arr[i]