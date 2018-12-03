
with open('files/day_2_input.txt') as f:
    ids = [ id.strip() for id in f]

total_3 = 0
total_2 = 0

for i in ids:
    counts = {}
    for x in i:
        if( x in counts.keys() ):
            counts[x] += 1
        else:
            counts[x] = 1

    check_3 = False
    check_2 = False

    for i in counts:
        if(counts[i] == 3 and not check_3):
            check_3 = True
        elif(counts[i] == 2 and not check_2):
            check_2 = True

    if(check_3):
        total_3 += 1
    if(check_2):
        total_2 += 1


print('Part 1: ' + str(total_2*total_3))

#Part 2
id_length = len(ids[0])
for i in range(len(ids)):

    for j in range(i+1,len(ids)):


        num_different = 0
        for z in range(id_length):
            if( ids[i][z]!=ids[j][z] ):
                num_different += 1
                if(num_different > 1):
                    break


        if(num_different == 1):
            final_answer = ''
            for z in range(id_length):
                if( ids[i][z]!=ids[j][z] ):
                    continue
                else:
                    final_answer += ids[i][z]
            print('Part 2: ' + str(final_answer))
            exit()



