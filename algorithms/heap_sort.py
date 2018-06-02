class HeapSort:
    def __init__(self, data):
        self.data = data
        self.sort()

    def heapify(self, data, heap_size, index):
        largest = index                 # Index of node's parent
        left_index = 2 * index + 1      # Index of left child branch
        right_index = 2 * index + 2     # Index of right child branch

        # Check that left child of root exists and is greater than root
        if left_index < heap_size and data[index] < data[left_index]:
            largest = left_index

        # Check that right child of root exists and is greater than root
        if right_index < heap_size and data[largest] < data[right_index]:
            largest = right_index

        # Move largest item to the end and heapify the root
        if largest != index:
            data[index], data[largest] = data[largest], data[index]
            self.heapify(data, heap_size, largest)

    def sort(self):
        heap_size = len(self.data)

        # Heapify the data by building a maxheap
        for i in range(heap_size, -1, -1):
            self.heapify(self.data, heap_size, i)

        # Heapify next root element
        for i in range(heap_size - 1, 0, -1):
            print(self.data)
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(self.data, i, 0)

        print("Sorted data: {}".format(self.data))
        return
