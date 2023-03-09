from iterative_solution import find_median_from_two_sorted_arrays_iterative
from recursive_solution import find_median_from_two_sorted_arrays_recursive
import time
import matplotlib.pyplot as plt

dataset_size_list = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]
results_list = [500000.5, 1000000.5, 1500000.5, 2000000.5, 2500000.5, 3000000.5, 3500000.5, 4000000.5, 4500000.5, 5000000.5]

iterative_time_list = []
recurive_time_list = []

for dataset_size_index in range(len(dataset_size_list)):
    dataset_size = dataset_size_list[dataset_size_index]
    #print ("Dataset Size : ", dataset_size)
    median_expected_result = results_list[dataset_size_index]
    #print (median_expected_result)
    
    list_1 = []
    list_2 = []
    for i in range(1, dataset_size+1):
        if (i%2 == 0):
            list_1.append(i)
        else:
            list_2.append(i)

    iterative_time = time.time()
    actual_median = find_median_from_two_sorted_arrays_iterative(list_1, list_2)
    #print (actual_median)
    assert median_expected_result == actual_median  # To verify the result
    end = time.time()
    iterative_time = end - iterative_time

    recursive_time = time.time()
    actual_median = find_median_from_two_sorted_arrays_recursive(list_1, list_2)
    #print (actual_median)
    assert median_expected_result == actual_median  # To verify the result
    end = time.time()
    recursive_time = end - recursive_time
    
    iterative_time_list.append(iterative_time)
    recurive_time_list.append(recursive_time)  

print ("All Test Cases Passed")
print (iterative_time_list)
print (recurive_time_list)


# Plotting the Iterative Solution Results 

plt.plot(dataset_size_list, iterative_time_list)    # plotting the points
plt.xlabel('Dataset Size')                          # naming the x axis
plt.ylabel('Time (Milli-Seconds)')                  # naming the y axis
plt.title('Iterative Solution Results')             # giving a title to the graph
plt.show()                                          # display the plot

# Plotting the Recursive Solution Results 

plt.plot(dataset_size_list, recurive_time_list) # plotting the points
plt.xlabel('Dataset Size')                      # naming the x axis
plt.ylabel('Time (Milli-Seconds)')              # naming the y axis
plt.title('Recursive Solution Results')         # giving a title to the graph
plt.show()                                      # display the plot
