def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(0, i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

def selection_sort(list):
    for i in range(len(list)-1, 0, -1):
        max_number_position = 0
        for j in range(1, i+1):
            if list[j] > list[max_number_position]:
                max_number_position = j
        list[max_number_position], list[i] = list[i], list[max_number_position]

def merge(list, start, medium, end):
    pass
    """
    n1 = m - l + 1
	n2 = r- m
	L = [0] * (n1)
	R = [0] * (n2)
	for i in range(0 , n1):
		L[i] = arr[l + i]
	for j in range(0 , n2):
		R[j] = arr[m + 1 + j]
	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2 :
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
    """
def merge_sort(list, start, end):
    if len(list) <= 1:
        return
    else:
		middle = (start+(end-1))/2
        print(middle)
        merge_sort(list, start, middle)
    	merge_sort(list, middle+1, end)
    	merge(list, start, medium, end)

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
            print(list)
        list[j+1] = key
        print(list)

if __name__=="__main__":
    list = [49, 91, 11, 39, 98, 66, 24, 70, 3, 16]
    #bubble_sort(list)
    #print(list)
    #selection_sort(list)
    #print(list)
    #insertion_sort(list)
    #print(list)
    merge_sort(list, 0, len(list))
    print(list)
