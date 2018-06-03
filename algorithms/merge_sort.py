class MergeSort:
    def __init__(self, data):
        self.data = data

    def sort(self, data):

        data_length = len(data)
        if data_length > 1:

            # Divide the data into 2 halves and recursevely merge them
            midpoint = data_length // 2
            left_half = self.sort(data[:midpoint])
            right_half = self.sort(data[midpoint:])

            i = j = k = 0       # Initial indexes of subarrays
            left_half_length = len(left_half)
            right_half_length = len(right_half)

            while i < left_half_length and j < right_half_length:
                # Swap elements in provided data with the smallest element in the two halves
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < left_half_length:
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < right_half_length:
                data[k] = right_half[j]
                j += 1
                k += 1

            print("Left half: {}\nRight half: {}".format(left_half, right_half))
        return data
