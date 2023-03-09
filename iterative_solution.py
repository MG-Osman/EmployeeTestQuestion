def find_median_from_two_sorted_arrays_iterative(list_1, list_2):
    i = 0
    j = 0
    merged_list = []
    while (i<len(list_1) or j<len(list_2)):
        if (i == len(list_1)):
            merged_list.append(list_2[j])
            j += 1
        elif (j == len(list_2)):
            merged_list.append(list_1[i])
            i += 1  
        elif (list_1[i] <= list_2[j]):
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1

    if (len(merged_list)%2 == 0):
        median = (merged_list[len(merged_list)//2 - 1] + merged_list[len(merged_list)//2])/2
    else:
        median = merged_list[len(merged_list)//2]

    return median
