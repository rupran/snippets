import heapq
import random

N = 199999

lst = []
for elem in range(1, N+1):
    lst.append(elem)

random.shuffle(lst)

pctile = 50
# Left heap (max-heap) contains elements smaller than the current pctile,
# right heap (min-heap, heapq default) the pctile and all bigger elements.
left = []
right = []
for elem in lst:
    if len(right) == 0:
        heapq.heappush(right, elem)
    else:
        cur_pctile = right[0]
        if elem < cur_pctile:
            heapq.heappush(left, -elem)
        else:
            heapq.heappush(right, elem)

        # Rebalance heaps if necessary
        part_in_left = float(len(left))/float(len(left) + len(right))
        if part_in_left < float(pctile)/100:
            # Right heap became too big
            top = heapq.heappop(right)
            heapq.heappush(left, -top)

        # Recalculate, as previous rebalance could have made left heap bigger
        # than right heap, and for odd numbers we would like to have the right
        # heap to be one element bigger than the left heap (correct pctile).
        part_in_left = float(len(left))/float(len(left) + len(right))
        if part_in_left > float(pctile)/100:
            # Left heap became too big
            top = heapq.heappop(left)
            heapq.heappush(right, -top)

print len(left)
print len(right)
        
# This is the element constituting the wanted percentile
print right[0]
