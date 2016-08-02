import random

# to is exclusive
def binary_search(lst, fro, to, looking_for):
    while fro != to:
        mid = fro + (to - fro)/2
        if lst[mid] > looking_for:
            to = mid
        else:
            fro = mid + 1
    return fro

def find_closest(lst, lfo):
    idx = binary_search(lst, 0, len(lst), lfo)
    if idx == 0:
        return 0
    if idx == len(lst):
        return idx - 1
    if lst[idx] - lfo > lfo - lst[idx - 1]:
        return idx - 1
    else:
        return idx

lst = []
for i in range(0, 100):
    if random.random() > 0.75:
        lst.append(i)
print lst

lfo = 50
print "Looking for " + str(lfo)
ret = find_closest(lst, lfo)

print "returned index is " + str(ret) + "(" + str(lst[ret]) + ")"
