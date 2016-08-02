import random
import numpy

class Sorter:

    def __init__(self, lst):
        self.lst = lst
        self.counter = 0

    def getPivot(self, start, end):
        retval = numpy.median([self.lst[start], self.lst[(start+end)/2], self.lst[end]])
        return retval

    def swap(self, in_a, in_b):
        tmp = self.lst[in_a]
        self.lst[in_a] = self.lst[in_b]
        self.lst[in_b] = tmp
        self.counter += 1

    def qsort(self, start, end):
        if start < end:
            p = self.partition(start, end)
            self.qsort(start, p)
            self.qsort(p+1, end)

    def partition(self, start, end):
        pivot = self.getPivot(start, end)
        i = start
        j = end
        while True:
            while(self.lst[i] < pivot):
                i += 1
            while(self.lst[j] > pivot):
                j -= 1
            if i >= j:
                return j
            self.swap(i, j)

lst = list(range(1, 100))
random.shuffle(lst)
print lst
sorter = Sorter(lst)
sorter.qsort(0, len(lst)-1)
print sorter.lst
print sorter.counter
