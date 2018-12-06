from datetime import *
import operator

with open('files/day_4_input.txt') as f:
    inputs = [ inp.strip() for inp in f]

inputs.sort(key=lambda date: datetime.strptime( date[ date.index('[')+1:date.index(']') ] , "%Y-%m-%d %H:%M"))
#print(inputs)

guards = {}
guards_start_times = {}
guards_end_times = {}

for j in range(len(inputs)):
    i = inputs[j]
    if( i[i.index(']')+ 2]  == 'G' ):
        guard_id = i[i.index('#')+1:i.index('b')-1]
        j += 1
        i = inputs[j]

        check_slept = False
        check_woke = False
        
        while( not i[i.index(']')+ 2] == 'G' ):
            if(not check_slept and i[i.index(']')+ 2] == 'f'):
                start_time = datetime.strptime( i[ i.index('[')+1:i.index(']') ], "%Y-%m-%d %H:%M") 
                check_slept = True

                if(guard_id in guards_start_times.keys()):
                    guards_start_times[guard_id].append(start_time)
                else:
                    guards_start_times[guard_id] = [start_time]

            if(not check_woke and i[i.index(']')+ 2] == 'w'):
                end_time = datetime.strptime( i[ i.index('[')+1:i.index(']') ] , "%Y-%m-%d %H:%M")
                check_woke = True

                if(guard_id in guards_end_times.keys()):
                    guards_end_times[guard_id].append(end_time)
                else:
                    guards_end_times[guard_id] = [end_time]
            
            if(check_slept and check_woke):
                total = (end_time-start_time).total_seconds()
                check_slept = False
                check_woke = False

                if( guard_id in guards.keys() ):
                    guards[guard_id] += total
                else:
                    guards[guard_id] = total


            j += 1
            if(j>len(inputs)-1):
                break
            i = inputs[j]



def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

best_guard = max(guards.iteritems(), key=operator.itemgetter(1))[0]
len_times = len(guards_start_times[max(guards.iteritems(), key=operator.itemgetter(1))[0]])

all_mins = {}


for i in range(len_times):
    # print(guards_start_times[best_guard][i] )
    # print(guards_end_times[best_guard][i] )
    
    for result in perdelta(guards_start_times[best_guard][i], guards_end_times[best_guard][i], timedelta(minutes=1)):
        result = result.minute
        if(result in all_mins.keys()):
            all_mins[result] += 1
        else:
            all_mins[result] = 1
print("Part 1:")
print("Guard id: ",best_guard)
print("(Minute,Number of Times) = ",max(all_mins.iteritems(),key=operator.itemgetter(1)))

guard_mins = {}
global_max = 0
for guard in guards.keys():
    len_times = len(guards_start_times[guard])
    # print(guard,len_times)
    all_mins = {}

    for i in range(len_times):
        # print(guards_start_times[guard][i] )
        # print(guards_end_times[guard][i] )
        for result in perdelta(guards_start_times[guard][i], guards_end_times[guard][i], timedelta(minutes=1)):
            if(guards_start_times[guard][i].hour == guards_end_times[guard][i].hour ):
                hour = 0
            else:
                hour = 1
            minu = result.minute

            to_key = minu
            if(to_key in all_mins.keys()):
                all_mins[to_key] += 1
            else:
                all_mins[to_key] = 1    

    guard_mins[guard] = all_mins
    
    if(max(all_mins.iteritems(),key=operator.itemgetter(1))[1] > global_max ):
        global_max = max(all_mins.iteritems(),key=operator.itemgetter(1))[1]
        best_guard = guard

# print(guard_mins)
# for i in guard_mins.keys():
print("\nPart 2:")

print("Guard id: ",best_guard)
print("(Minute,Number of Times) = ",global_max)

#179,30