# Create a helper Swap function
def swap(my_list: list[int], index1: int, index2: int) -> None:
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# Create a helper Pivot function
def pivot(my_list: list[int], pivot_index: int, end_index: int) -> int:
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

# Create a Quick Sort algorithm
def quick_sort_helper(my_list: list[int], left: int, right: int) -> list[int]:
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list: list[int]) -> list[int]:
    return quick_sort_helper(my_list, 0, len(my_list)-1)

quick_sort([4, 6, 1, 7, 3, 2, 5])