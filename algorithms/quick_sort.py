def quick_sort(data):
    data_length = len(data)
    if data_length <= 1:
        return data
    else:
        pivot = data[0]
        larger_items = [item for item in data[1:] if item > pivot]
        smaller_items = [item for item in data[1:] if item <= pivot]
        print("Pivot: {}\nLarger: {}\nSmaller: {}".format(
            pivot, larger_items, smaller_items))
        return(quick_sort(smaller_items) + [pivot] + quick_sort(larger_items))
