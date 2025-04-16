#include "sort.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * print_segment - prints a segment of the array in the required format.
 * @array: The array to print.
 * @start: Start index (inclusive).
 * @end: End index (exclusive).
 */
void print_segment(int *array, int start, int end)
{
    int i;

    for (i = start; i < end; i++)
    {
        printf("%d", array[i]);
        if (i < end - 1)
            printf(", ");
    }
    printf("\n");
}

/**
 * merge - merges two sorted subarrays and prints the merging process.
 * @array: The array containing the subarrays.
 * @temp: The temporary array used for merging.
 * @left: The left index of the segment.
 * @mid: The index separating the two sorted subarrays.
 * @right: The right index (exclusive) of the segment.
 */
void merge(int *array, int *temp, int left, int mid, int right)
{
    int i = left, j = mid, k = left;

    printf("Merging...\n");
    printf("[left]: ");
    print_segment(array, left, mid);
    printf("[right]: ");
    print_segment(array, mid, right);

    /* Merge the two halves into temp */
    while (i < mid && j < right)
    {
        if (array[i] <= array[j])
        {
            temp[k] = array[i];
            i++;
        }
        else
        {
            temp[k] = array[j];
            j++;
        }
        k++;
    }
    while (i < mid)
    {
        temp[k] = array[i];
        i++;
        k++;
    }
    while (j < right)
    {
        temp[k] = array[j];
        j++;
        k++;
    }

    /* Copy back to original array */
    for (i = left; i < right; i++)
        array[i] = temp[i];

    printf("[Done]: ");
    print_segment(array, left, right);
}

/**
 * merge_recursive - recursively divides and merges the array.
 * @array: The array to sort.
 * @temp: The temporary array used for merging.
 * @left: The starting index (inclusive) for this recursion.
 * @right: The ending index (exclusive) for this recursion.
 */
void merge_recursive(int *array, int *temp, int left, int right)
{
    int mid;

    if (right - left < 2)
        return;

    /* For odd lengths, left side will have fewer elements */
    mid = left + (right - left) / 2;
    merge_recursive(array, temp, left, mid);
    merge_recursive(array, temp, mid, right);
    merge(array, temp, left, mid, right);
}

/**
 * merge_sort - sorts an array of integers in ascending order using
 *              the Merge Sort algorithm (top-down approach).
 * @array: The array of integers.
 * @size: The size of the array.
 */
void merge_sort(int *array, size_t size)
{
    int *temp;

    if (array == NULL || size < 2)
        return;

    /* Only one malloc call is allowed for the temporary array */
    temp = malloc(sizeof(int) * size);
    if (temp == NULL)
        return;

    merge_recursive(array, temp, 0, size);
    free(temp);
}
