import operator
with open('files/day_6_input.txt') as f:
    inputs = [ inp.strip() for inp in f]
# print(inputs)

points = []
for i in inputs:
    points.append( [int(x) for x in i.split(',')] )
# print(points)

min_x=300
min_y=300
max_x=0
max_y=0
for i in range(len(points)):
    if(points[i][0] < min_x):
        min_x = points[i][0]
    if(points[i][0] > max_x ):
        max_x = points[i][0]
    if(points[i][1] < min_y ):
        min_y = points[i][1]
    if(points[i][1] > max_y ):
        max_y = points[i][1]

# print(min_x,max_x,min_x,min_y)
min_x = min_x -1

max_x = max_x +1
min_y = min_y -1
max_y = max_y +1

def manhattan(x1,y1,x2,y2):
    dist = abs(x1-x2) + abs(y1-y2)
    return(dist)

matrix = []

for i in range(0,max_x):
    col = []
    for j in range(0,max_y):
        min_manhattan = 500
        equals = []
        for k in range(len(points)):
            
            if( manhattan( i,j,points[k][0],points[k][1] ) <= min_manhattan ):
                min_manhattan = manhattan( i,j,points[k][0],points[k][1] )
                best_manhattan = k

                if(min_manhattan in equals):
                    equals.append(min_manhattan)
                else:
                    equals = [min_manhattan]
                
                # print(i,j,points[best_manhattan])
        # print(equals)
        if(len(equals)>1 ):
            col.append('.')
        else:
            col.append(best_manhattan)
    matrix.append(col)

boundary_indexes = []
# print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # print(matrix[i][j])
        if(i==0 or i == len(matrix[0]) or j == 0 or j == len(matrix)):
            if( not matrix[i][j] in boundary_indexes ):
                boundary_indexes.append(matrix[i][j])

# print(boundary_indexes)

area_covered = {}
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # print(matrix[i][j])        
        if( not matrix[i][j] in boundary_indexes ):
            if(matrix[i][j] in area_covered.keys()):
                area_covered[matrix[i][j]] += 1
            else:
                area_covered[matrix[i][j]] = 1

print('Part 1:')
print( max(area_covered.iteritems(),key=operator.itemgetter(1))[1] )

region_size = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        total_distance = 0
        for k in range(len(points)):
            total_distance += manhattan( i,j,points[k][0],points[k][1] )
            if(total_distance>10000):
                break
        if(total_distance<10000):
            region_size += 1
print(region_size)

ff = open("files/day_6_matrix.txt","w")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        ff.write(str(matrix[i][j])+',')
    ff.write('\n')