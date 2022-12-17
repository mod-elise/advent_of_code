import json

def compare_lists(left, right, index):
    for r in range (index, len(left)+1, 1):
        if (r > (len(right)-1) or (not right)):
            return False
        if (r > (len(left)-1) or (not left)):
            return True
        if isinstance(left[r], int):
            left[r] = [left[r]]
        if isinstance(right[r], int):
            right[r] = [right[r]]
        try:
            if left[r] < right[r]:
                return True
            elif left[r] > right[r]:
                return False
            else:
                pass
        except:
            #feel filthy using an exception as a legit path, and I should be arrested for recursing at this point
            return (compare_lists(left[r], right[r], 0))
    print()
    return False

with open('day13_input_file') as f:
    signal_streams = f.readlines()


signal_pairs    = []
signals         = []
div_pack_1      = [[2]]
div_pack_2      = [[6]]

for signal_stream in signal_streams:
    if signal_stream != '\n':
        signal_pairs.append(json.loads(signal_stream))

for r in range (0, len(signal_pairs),2):
    left = signal_pairs[r]
    right = signal_pairs[r+1]

    for s in range (0, len(left),1):
        if isinstance(left[s], int):
            left[s] = [left[s]]
    for s in range (0, len(right),1):
        if isinstance(right[s],int):
            right[s] = [right[s]]

index_sum = 0   
div1_loc = 1    # when inserted it will be one after the last item it is greater than
div2_loc = 2    # when inserted into the list, it will be after div1_loc so add one

#part 1
for r in range (0, len(signal_pairs),2):
    list_ordered = compare_lists(signal_pairs[r], signal_pairs[r+1],0)
    if list_ordered:
        index_sum += (r//2)+1  #index starts at 1, not zero
    else:
        pass

#part 2
for signal_pair in signal_pairs:
    list_ordered = compare_lists(signal_pair, div_pack_1,0)
    if list_ordered:
        div1_loc +=1
    else:
        pass

for signal_pair in signal_pairs:
    list_ordered = compare_lists(signal_pair, div_pack_2,0)
    if list_ordered:
        div2_loc +=1
    else:
        pass

print (f'part 1 answer is {index_sum}')
print (f'part 2 answer is {div1_loc * (div2_loc)}')
