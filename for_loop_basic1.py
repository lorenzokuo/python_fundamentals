# 1. Basic - Print all the numbers/integers from 0 to 150.
for count in range(0,151):
	print(count)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
# solution 1
# count = 1
# while count < 1000000:
# 	print(count*5)
# 	count += 1

# solution 2
for count in range(1,1000001):
	print(count*5)

# 3. Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for count in range(1,101):
	if count%10 == 0:
		print("Dojo")
	elif count%5 == 0:
		print("Coding")
	else:
		print(count)


# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for count in range(0,500000):
	if count % 2 == 1:
	    sum += count

print (sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
count = 2018
while count >= 0:
	print(count)
	count -= 4

if count < 0:
	print(0)
# 6. Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
def flexCount(lowNum, highNum, mult):
	for i in range(lowNum, highNum+1):
		if i % mult == 0:
			print(i)

flexCount(2,9,3)




# predict the output
# 1
3
5
1
2

# 2
error

# 3
0
1
2
3
