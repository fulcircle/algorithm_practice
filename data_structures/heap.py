class MaxHeap:

    def __init__(self, arr):
        self.arr = arr
        self.build_heap()

    def build_heap(self):

        for i in range(len(self.arr) // 2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2

        largest = i
        if l < len(self.arr) and self.arr[l] > self.arr[largest]:
            largest = l

        if r < len(self.arr) and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
            self.max_heapify(largest)

    def push(self, val):
        self.arr.append(val)
        self.build_heap()

    def pop(self):
        if len(self.arr) > 0:
            val = self.arr.pop(0)

            if len(self.arr) > 0:
                last_item = self.arr.pop()
                self.arr.insert(0, last_item)
                self.build_heap()

            return val

        return None

arr = [1, 2, 3, 4, 5, 6, 7, 8]
m = MaxHeap(arr)
m.pop()
m.pop()
m.push(8)
print(m.arr)
