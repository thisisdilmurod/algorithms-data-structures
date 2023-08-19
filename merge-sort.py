# Create a helper Merge function
def merge(list1: list, list2: list) -> list:
    combined = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list[i] < list[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

# Create a Merge Sort algorithm
def merge_sort(my_list: list) -> list:
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left, right = merge_sort(my_list[:mid_index]), merge_sort(my_list[mid_index:])
    return merge(left, right)