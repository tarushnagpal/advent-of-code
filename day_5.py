f = open("files/day_5_input.txt")
text = f.read()
import operator


items = []
text_chars = []

for i in text:
    items.append(i)
    text_chars.append(i)


change = True
while(change):
    change = False
    for i in range(len(items)):
        if(i+1<len(items)):
            if( abs(ord(items[i]) - ord(items[i+1])) == 32 ):
                del(items[i])
                del(items[i])
                change = True

print(len(items))

total_changes = {}

for j in range(97,122):
    new_items = []
    new_items = [x for x in text_chars]
    change = True
    total_change = 0
    
    worst_ord = j
    items_to_check = []

    for i in range(len(new_items)):
        try:        
            if( (ord(new_items[i])==worst_ord) or (ord(new_items[i])+32==worst_ord) ):
                pass
            else:
                items_to_check.append(new_items[i])
            
        except:
            pass

    while(change):
        change = False
        for i in range(len(items_to_check)):
            if(i+1<len(items_to_check)):
                if( (abs(ord(items_to_check[i]) - ord(items_to_check[i+1])) == 32) ):
                    del(items_to_check[i])
                    del(items_to_check[i])
                    change = True
                    total_change += 1

    total_changes[j] = len(items_to_check)
    
global_max = min(total_changes.iteritems(),key=operator.itemgetter(1))
print(global_max)

