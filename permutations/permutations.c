#include <assert.h>
#include <stdbool.h>

void swap(int *arr, int i, int j) {
	int copy = arr[i];
	arr[i] = arr[j];
	arr[j] = copy;
}

int find_max(int arr[], int start, int stop) {
	int max = start;
	for (int i = start; i < stop; i++)
		if (arr[i] > arr[max])
			max = i;
	return max;
}

void sort_from(int arr[], int arr_len, int start) {
	int i = arr_len-1;
	while (i >= start) {
		int max = find_max(arr, start, i+1);
		swap(arr, i, max);
		i--;
	}
}

int find_successor(int *arr, int start, int arr_len, int i) {
	int lim = arr[find_max(arr, start, arr_len)] * 2;
	int j = 1;
	while (1) {
		for (int k = start; k < arr_len; k++)
			if (arr[k] == arr[i]+j)
				return k;
		j++;
		if (j > lim) break;
	}
	return i;
}

void p_callback(int *arr, int arr_len);

void permutations(int *arr, int arr_len, int start, int end) {
	for (int z = 0; z < end+1-start; z++) {
		if (end-start == 1)
			p_callback(arr, arr_len);
		
		if (end-start > 1)
			permutations(arr, arr_len, start+1, end);

		int s = find_successor(arr, start, arr_len, start);
		swap(arr, s, start);
		sort_from(arr, arr_len, start+1);
	}
}

bool assert_array_equals(int *arr1, int *arr2, int len) {
	for (int i = 0; i < len; i++)
		if (arr1[i] != arr2[i])
			return false;
	return true;
}

void p_callback(int *arr, int arr_len) {
	print_array(arr, arr_len);
}

void run_tests() {
	printf("Finding max of ");
	int arr1[11] = {1, 2, 3, 4, 11, 10, 9, 8, 7, 6, 5};
	print_array(arr1, 11);
	int max = find_max(arr1, 4, 11);
	printf("Found max: %d\n", max);
	assert(max == 4);

	printf("Sorting array ");
	int arr2[11] = {1, 2, 3, 4, 11, 10, 9, 8, 7, 6, 5};
	print_array(arr2, 11);
	sort_from(arr2, 11, 5);
	int arr_sorted[11] = {1, 2, 3, 4, 11, 5, 6, 7, 8, 9, 10};
	printf("Sorted array (from 5): ");
	print_array(arr2, 11);
	assert(assert_array_equals(arr2, arr_sorted, 10)); 

	printf("Finding successor of 5 in");
	int arr3[11] = {1, 2, 3, 4, 11, 10, 9, 8, 7, 6, 5};
	print_array(arr3, 11);
	int s = find_successor(arr3, 6, 11, 10);
	printf("Found successor at %d\n", s);
	assert(s == 9);
}

int main()
{
	// Uncomment to run tests.
	//run_tests();
	//exit();

	int arr[4] = {0, 1, 2, 3};
	permutations(arr, 4, 0, 3);

	return 0;
}
