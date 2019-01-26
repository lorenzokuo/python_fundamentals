# 1. Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def makeItBig(arr):
	for i in range(0,len(arr)):
		if arr[i]>0:
			arr[i]="big"
	return arr

makeItBig([-1,2,5,-5])
# 2. Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def countPositives(arr):
	count = 0
	for i in range(0,len(arr)):
		if arr[i]>0:
			count+=1
	arr[len(arr)-1]=count
	return arr

countPositives([-1,1,1,1])


# 3. SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumTotal(arr):
	sum = 0
	for i in range(0,len(arr)):
		sum +=arr[i]
	return sum

sumTotal([1,2,3,4])

# 4. Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def multiples(arr):
	avg = 0
	sum = 0
	for i in range(0,len(arr)):
		sum += arr[i]
	avg = sum/len(arr)
	return avg

multiples([1,2,3,4])


# 5. Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
def length(arr):
	return len(arr)

length([1,2,3,4])


# 6. Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum(arr):
	min = arr[0]
	if len(arr)<1:
		return False
	else:
		for i in range(0,len(arr)):
			if arr[i]<min:
				min = arr[i]
	return min

minimum([1,2,3,4])
minimum([-1,-2,-3])

# 7. Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def maximum(arr):
	max = arr[0]
	if len(arr)<1:
		return False
	else:
		for i in range(0,len(arr)):
			if arr[i]>max:
				max = arr[i]
	return max

maximum([1,2,3,4])
maximum([-1,-2,-3])


# 8. UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ultimateAnalyze(arr):
	sum = 0
	avg = 0
	min = arr[0]
	max = arr[0]
	for i in range(0,len(arr)):
		sum+=arr[i]
		if arr[i]<min:
			min = arr[i]
		if arr[i]>max:
			max = arr[i]
	avg = sum/len(arr)
	return sum,avg,min,max,len(arr)

ultimateAnalyze([1,2,3,4,5])


# 9. ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverseList(arr):
	for i in range(0,int(len(arr)/2)):
		temp = arr[i]
		arr[i] = arr[len(arr)-i-1]
		arr[len(arr)-i-1] = temp
	return arr

reverseList([1,2,3,4])

# solution 1
# def reverseList(arr):
# 	arr.reverse()
# 	return arr

# reverseList([1,2,3,4])

# solution 2 //extended slices//
# def reverseList(arr):
# 	return arr[::-1]

# reverseList([1,2,3,4])

# solution 3
# def reverseList(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1
#     return A

# reverseList([1,2,3,4,5],0,4)








