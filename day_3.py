with open('files/day_3_input.txt') as f:
    locations = [location for location in f]
fabric_matrix = []

for i in range(1000):
    fabric_cols = []
    for y in range(1000):
        fabric_cols.append('*')
    fabric_matrix.append(fabric_cols)

# Part 1
num_blocked = 0

for x in locations:

    pos_x = int(x[ x.index('@') + 1:x.index(':')].split(',')[0])
    pos_y = int(x[ x.index('@') + 1:x.index(':')].split(',')[1])
    len_x = int( x[x.index(':')+1:].split('x')[0] )
    len_y = int( x[x.index(':')+1:].split('x')[1] )
    
    total_len = len_x*len_y
    
    for i in range(len_x):
        for j in range(len_y):
            if( fabric_matrix[pos_x+i][pos_y+j] == '*' ):
                fabric_matrix[pos_x+i][pos_y+j] = '#'
            elif(fabric_matrix[pos_x+i][pos_y+j] == '#'):
                fabric_matrix[pos_x+i][pos_y+j] = 'X'
                num_blocked += 1

print("Part 1: " + str(num_blocked))

# Part 2
for x in locations:
    pos_x = int(x[ x.index('@') + 1:x.index(':')].split(',')[0])
    pos_y = int(x[ x.index('@') + 1:x.index(':')].split(',')[1])
    len_x = int( x[x.index(':')+1:].split('x')[0] )
    len_y = int( x[x.index(':')+1:].split('x')[1] )
    
    total_len = len_x*len_y
    check_unique = True
    
    for i in range(len_x):
        for j in range(len_y):
            if(fabric_matrix[pos_x+i][pos_y+j] == 'X' ):
                check_unique = False
                break
    
    if(check_unique):
        print( "Part 2: " + x[x.index('#'):x.index('@')-1] )
        break


        