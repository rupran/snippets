import random

# Implements a min-heap
def siftUp(heap, index):
    while True:
        if index == 0:
            break
        # Check if parent is bigger and possibly swap
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
    # Add new value at the end and restore heap property
    heap.append(val)
    siftUp(heap, len(heap)-1)

def removeMin(heap):
    n = len(heap)
    # Save minimum element for return
    retval = heap[0]
    # Swap last element to front and delete it at the end
    heap[0] = heap[n-1]
    del heap[n-1]
    # Restore heap property
    siftDown(heap, 0)
    return retval

def heapify(heap):
    for i in reversed(range((len(heap)-1)//2)):
        siftDown(heap, i)

# Test insertions
heap = []
for i in range(0, 11):
    insert(heap, i)

# Test removals
while heap:
    val = removeMin(heap)
    print "Removed " + str(val)
    print heap

# Test heapify
testheap = []
for i in range(0, 100):
    testheap.append(i)

array = testheap[:]
random.shuffle(testheap)
heapify(testheap)

result = []
while testheap:
    result += [removeMin(testheap)]

assert(result == sorted(array))
