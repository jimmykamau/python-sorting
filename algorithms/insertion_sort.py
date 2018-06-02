class InsertionSort:
    def __init__(self, data):
        self.data = data
        self.sort()

    def sort(self):
        for i in range(1, len(self.data)):
            print(self.data)
            while i > 0 and self.data[i] < self.data[i-1]:
                self.data[i], self.data[i-1] = \
                self.data[i-1], self.data[i]
                i -= 1
        
        print("Sorted list: {}".format(self.data))
        return
