# T diagram prediction
# 1
a() = 5
output
5

# 2
a() = 5
output
5+5 = 10

# 3
a() = 5
output
5

# 4
a() = 5
output
5

# 5
a() = 5
x = 5
output
none

# 6
b = 1, 2
c = 2, 3
a() = 3, 5
output
3
5
undefined

# 7 x (the output 25 should without '' as test shown)
b = 2
c = 5
a() = bc = 25
output
'25' x
# 25

# 8 x (misunderstanding my last return 7, which should not be excuted)
a() = 7
b = 100
output
7 x
# 100 (called by print(b) in def)
# 10 (return 10)

# 9
a() = 7,14
b = 2,5
c = 3,3
output
7
14
21

# 10
a() = 8
b = 3
c = 5
output
8

# 11
b = 500
a() = 300
output
500
500
300
500

# 12 x (missing one 300 in output. when a() called, should print once and return once so 300 and 300)
b = 500
a() = 300
output
500
500
300
# 300
500

# 13
b = 500, 300
a() = 300
output
500
500
300

# 14
a() = 1,3,2
b() = 3

output
1
3
2

# 15
a() = 1,3,5,10
x = 3,5
b() = 3,5
y = 1,3,5
output
10