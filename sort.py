import sys

from algorithms import heap_sort


def driver():
    algorithm = sys.argv[1]
    unsorted_data = sys.argv[2].split(',')
    unsorted_data = list(map(int, unsorted_data))

    if algorithm == "heap_sort":
        heap_sort.HeapSort(unsorted_data)


if __name__ == "__main__":
    driver()
