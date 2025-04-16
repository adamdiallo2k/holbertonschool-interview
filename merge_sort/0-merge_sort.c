#include <stdlib.h>
#include <stdio.h>
#include "sort.h"

/**
 * merge_sort_recursive - Sorts an array of integers in ascending order
 * using the Merge Sort algorithm
 * @array: The array to be sorted
 * @start: The starting index of the array
 * @end: The ending index of the array
 * @temp: A temporary array to store the sorted elements
 * Return: Nothing
 */
void merge_sort_recursive(int *array, size_t start, size_t end, int *temp)
{
size_t middle;

if (end - start <= 1)
return;

middle = start + (end - start) / 2;

merge_sort_recursive(array, start, middle, temp);
merge_sort_recursive(array, middle, end, temp);
merge(array, start, middle, end, temp);
}

/**
 * merge - Merges two sorted arrays into one sorted array
 * @array: The array to be sorted
 * @start: The starting index of the array
 * @middle: The middle index of the array
 * @end: The ending index of the array
 * @temp: A temporary array to store the sorted elements
 * Return: Nothing
 */
void merge(int *array, size_t start, size_t middle, size_t end, int *temp)
{
size_t i, j, k;

/* Initialize indices for the two subarrays and the temporary array */
i = start;
j = middle;
k = 0;

/* Print the subarrays being merged */
printf("Merging...\n[left]: ");
print_array(array + start, middle - start);
printf("[right]: ");
print_array(array + middle, end - middle);

/* Merge the two subarrays into the temporary array */
while (i < middle && j < end)
{
if (array[i] <= array[j])
temp[k++] = array[i++];
else
temp[k++] = array[j++];
}
/* Copy any remaining elements from the first subarray */
while (i < middle)
temp[k++] = array[i++];
/* Copy any remaining elements from the second subarray */
while (j < end)
temp[k++] = array[j++];
/* Copy the merged elements back to the original array */
for (i = 0; i < k; i++)
array[start + i] = temp[i];

printf("[Done]: ");
print_array(array + start, end - start);
}


/**
 * merge_sort - Sorts an array of integers in ascending order
 *
 * @array: The array to be sorted
 * @size: Number of elements in @array
 */
void merge_sort(int *array, size_t size)
{
int *temp;

if (array == NULL || size < 2)
return;

temp = malloc(size * sizeof(int));
if (!temp)
return;

merge_sort_recursive(array, 0, size, temp);

free(temp);
}
