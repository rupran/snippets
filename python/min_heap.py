# Implements a min-heap
def siftUp(heap, index):
    while True:
        if index == 0:
            break
        # Check if parent is bigger and swap
        parent = (index-1)//2
        if heap[parent] > heap[index]:
            tmp = heap[parent]
            heap[parent] = heap[index]
            heap[index] = tmp
        else:
            break
        # Repeat at parent
        index = parent

def siftDown(heap, index):
    while True:
        # Find smaller child
        leftC = index*2 + 1
        rightC = index*2 + 2
        smallerC = leftC
        if leftC >= len(heap):
            break
        if rightC < len(heap) and heap[rightC] < heap[smallerC]:
            smallerC = rightC
        # Swap if smaller child is smaller than current element
        if heap[smallerC] < heap[index]:
            tmp = heap[smallerC]
            heap[smallerC] = heap[index]
            heap[index] = tmp
        else:
            break
        # Move to child and repeat
        index = smallerC

def insert(heap, val):
    heap.append(val)
    siftUp(heap, len(heap)-1)

def removeMin(heap):
    n = len(heap)
    retval = heap[0]
    heap[0] = heap[n-1]
    del heap[n-1]
    siftDown(heap, 0)
    return retval

heap = []
for i in range(0, 11):
    insert(heap, i)

while heap:
    val = removeMin(heap)
    print "Removed " + str(val)
    print heap
