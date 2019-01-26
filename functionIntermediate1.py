# 1. randInt() returns a random integer between 0 to 100


# 2. randInt(max=50) returns a random integer between 0 to 50


# 3. randInt(min=50) returns a random integer between 50 to 100

# 4. randInt(min=50, max=500) returns a random integer between 50 and 500




# def randInt(min=0, max=100):
# 	return(int(random.uniform(min,max)))

def randInt(min=0, max=100):
    temp = int(random.random()*max)
    if temp < min:
	    temp += min
    return temp
