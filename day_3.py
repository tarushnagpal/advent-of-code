f = open('files/day_3_input.txt')
a = []

for i in range(1000):
    b = []
    for y in range(1000):
        b.append('*')
    a.append(b)

num_blocked = 0

for x in f:
    pos_x = int(x[ x.index('@') + 1:x.index(':')].split(',')[0])
    pos_y = int(x[ x.index('@') + 1:x.index(':')].split(',')[1])
    len_x = int( x[x.index(':')+1:].split('x')[0] )
    len_y = int( x[x.index(':')+1:].split('x')[1] )
    
    total_len = len_x*len_y
    check_unique = 0

    for i in range(len_x):
        for j in range(len_y):
            if(a[pos_x+i][pos_y+j] == '*' ):
                a[pos_x+i][pos_y+j] = '#'
            elif(a[pos_x+i][pos_y+j] == '#'):
                a[pos_x+i][pos_y+j] = 'X'
                num_blocked += 1

    if(check_unique == total_len):
        print(x)

print(num_blocked)


f2 = open('files/day_3_input.txt')
for x in f2:
    pos_x = int(x[ x.index('@') + 1:x.index(':')].split(',')[0])
    pos_y = int(x[ x.index('@') + 1:x.index(':')].split(',')[1])
    len_x = int( x[x.index(':')+1:].split('x')[0] )
    len_y = int( x[x.index(':')+1:].split('x')[1] )
    
    total_len = len_x*len_y
    check_unique = 0
    
    for i in range(len_x):
        for j in range(len_y):
            if(a[pos_x+i][pos_y+j] == '#' ):
                check_unique += 1
    
    if(check_unique == total_len):
        print(x)

