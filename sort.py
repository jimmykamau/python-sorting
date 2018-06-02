import sys

from algorithms import (
    heap_sort, quick_sort, insertion_sort)


def driver():
    algorithm = sys.argv[1]
    unsorted_data = sys.argv[2].split(',')
    unsorted_data = list(map(int, unsorted_data))

    if algorithm == "heap_sort":
        heap_sort.HeapSort(unsorted_data)
    if algorithm == "quick_sort":
        print(quick_sort.quick_sort(unsorted_data))
    if algorithm == "insertion_sort":
        insertion_sort.InsertionSort(unsorted_data)


if __name__ == "__main__":
    driver()
