# 1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  

# x[1] = [15,8,9]

for i in x:
	for j in i:
		if j == 10:
			j = 15

print(x)

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?

# solution 1
# students[0] = {'first_name':  'Michael', 'last_name' : 'Bryant'}

# solution2
# students[0]['last_name'] = 'Bryant'

for i in students:
    print(i)
    for j in i:
        print(i[j])
        if i[j] == 'Jordan':
            i[j] = 'Bryant'

print(students)

# For the sports_directory, how would you change 'Messi' to 'Andres'?

# solution 1
# sports_directory['soccer'] = ['Andres', 'Ronaldo', 'Rooney']

# solution 2
# sports_directory['soccer'][0] = 'Andres'

# solution 3 //right concept but cannot change value because of the issue of key and value.
# for i in sports_directory:
# 	print(sports_directory[i])
# 	for j in sports_directory[i]:
# 		print(j)
# 		if j == 'Messi':
# 		     j = 'Andres'


for i in sports_directory:
	for j in range(len(sports_directory[i])):
		if sports_directory[i][j] == 'Messi':
			sports_directory[i][j] = 'Andres'


# For z, how would you change the value 20 to 30?

# solution 1
# z[0]={'x': 10, 'y': 30}

# solution 2
for val in z.values():
    if val == 20:
        val = 30

print(z)

# solution 3
z[0]['y'] = 20

 # 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{'first_name' : 'John', 'last_name' : 'Rosales'},{'first_name' : 'Mark', 'last_name' : 'Guillen'},{'first_name' : 'KB', 'last_name' : 'Tonel'}]

# step 1 // items no attribute
# def iterateDictionary(x):
#     for key, val in x.items():
#         print (key, "-", val)

# iterateDictionary(students)

# step 2 // output continue without new line
# def iterateDictionary(x):
# 	for i in range(0,4):
# 	    for key, val in x[i].items():
# 	        print(key, '-', val, end=', ')

# iterateDictionary(students)

# solution!

def iterateDictionary(x):
    for i in x:
        for key, val in i.items():
            if key == 'last_name':
                print(key, '-', val)
            else:
                print(key, '-', val, end=', ')

iterateDictionary(students)

# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output

# first try // called each first and last name
# def iterateDictionary2(x):
# 	for i in range(0,4):
# 		for val in x[i].values():
# 		    print(val)

# iterateDictionary2(students)

def iterateDictionary2(key,x):
	for i in x:
		for key, val in i.items():
			if key == 'first_name':
				print(val)

iterateDictionary2('first_name',students)


# 4
dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}

# first try // coudn't print new line for each
# def printDojoInfo(y):
# 	for key, val in y.items():
# 		print(key, val)

# printDojoInfo(dojo)


def printDojoInfo(x):
	count = 7
	for i in x:
		print(count,i.upper())
		count+=1
		for j in range(len(x[i])):
			if j == len(x[i])-1:
				print(x[i][j],'\n')
			else:
				print(x[i][j])

printDojoInfo(dojo)

# use len() for counting

