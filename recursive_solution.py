import sys

INF = sys.maxsize

def find_median_from_two_sorted_arrays_recursive(list_1, list_2):
    m = len(list_1)
    n = len(list_2)
    total_length = m + n
    target = int(total_length/2)

    if (total_length % 2 == 0):
        return (find_k_th(list_1, list_2, 0, 0, target) + find_k_th(list_1, list_2, 0, 0, target + 1)) / 2
    else:
        return find_k_th(list_1, list_2, 0, 0, target + 1)

def find_k_th(a, b, start_1, start_2, k):
    if (start_1 >= len(a)):
        return b[start_2 + k - 1]
    if (start_2 >= len(b)):
        return a[start_1 + k - 1]
    if (k == 1):
        return min(a[start_1], b[start_2])

    list_1_mid_index = start_1 + k // 2 - 1
    list_2_mid_index = start_2 + k // 2 - 1

    if (list_1_mid_index >= len(a)):
        mid_1 = INF
    else:
        mid_1 = a[list_1_mid_index]

    if (list_2_mid_index >= len(b)):
        mid_2 = INF
    else:
        mid_2 = b[list_2_mid_index]

    if (mid_1 > mid_2):
        return find_k_th(a, b, start_1, start_2 + k // 2, k - k // 2)
    else:
        return find_k_th(a, b, start_1 + k // 2, start_2, k - k // 2)

