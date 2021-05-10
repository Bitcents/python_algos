import sys

class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.Heap = [0]*(self.max_size + 1)
        self.FRONT = 1
        self.Heap[0] = -1 * sys.maxsize

    def parent(self, pos):
        return pos//2
    
    def left_child(self, pos):
        return pos*2
    
    def right_child(self, pos):
        return pos*2 + 1

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def is_leaf(self, pos):
        if pos >= self.size//2 and pos <= self.size:
            return True
        else:
            return False

    def heapify(self, pos):
        if not self.is_leaf(pos):
            if self.Heap[pos] > self.Heap[self.left_child(pos)]:
                self.swap(pos, self.left_child(pos))
                self.heapify(self.left_child(pos))
            
            elif self.Heap[pos] > self.Heap[self.right_child(pos)]:
                self.swap(pos, self.right_child(pos))
                self.heapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size+= 1
        self.Heap[self.size] = element

        current = self.size
        
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        min_value = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.heapify(self.FRONT)
        return min_value

    def print_heap(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))
 
    # Function to build the min heap using
    # the minHeapify function
    def create_min_heap(self):
 
        for pos in range(self.size//2, 0, -1):
            self.heapify(pos)

if __name__ == "__main__":
     
    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.create_min_heap()
    
    minHeap.print_heap()
    print("The Min val is " + str(minHeap.remove()))