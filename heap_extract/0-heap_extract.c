#include "binary_trees.h"
#include <stdlib.h>

/**
 * swap_values - Swaps the values between two nodes.
 * @a: First node.
 * @b: Second node.
 */
void swap_values(heap_t *a, heap_t *b)
{
    int temp = a->n;
    a->n = b->n;
    b->n = temp;
}

/**
 * heapify_down - Restores the Max Heap property by sifting a node downwards.
 * @node: Node to heapify down from.
 */
void heapify_down(heap_t *node)
{
    heap_t *largest = node;
    heap_t *left = node->left;
    heap_t *right = node->right;

    if (left && left->n > largest->n)
        largest = left;
    if (right && right->n > largest->n)
        largest = right;

    if (largest != node)
    {
        swap_values(node, largest);
        heapify_down(largest);
    }
}

/**
 * find_last_node - Finds the last node in level-order of the binary heap.
 * @root: Pointer to the root node of the heap.
 * Return: Pointer to the last node.
 */
heap_t *find_last_node(heap_t *root)
{
    heap_t *last = NULL;
    heap_t *current;
    size_t front = 0, rear = 0;
    heap_t *queue[1024]; /* Assuming heap size won't exceed 1024 nodes */

    if (!root)
        return (NULL);

    queue[rear++] = root;
    while (front < rear)
    {
        current = queue[front++];
        last = current;

        if (current->left)
            queue[rear++] = current->left;
        if (current->right)
            queue[rear++] = current->right;
    }
    return (last);
}

/**
 * heap_extract - Extracts the root node of a Max Binary Heap.
 * @root: Double pointer to the root node of the heap.
 * Return: Value stored in the root node, or 0 on failure.
 */
int heap_extract(heap_t **root)
{
    heap_t *last, *parent;
    int extracted_value;

    if (!root || !(*root))
        return (0);

    extracted_value = (*root)->n;

    /* Find the last node in the heap */
    last = find_last_node(*root);
    if (!last)
        return (0);

    /* If the last node is the root itself */
    if (last == *root)
    {
        free(*root);
        *root = NULL;
        return (extracted_value);
    }

    /* Replace root's value with the last node's value */
    (*root)->n = last->n;

    /* Remove the last node */
    parent = last->parent;
    if (parent->left == last)
        parent->left = NULL;
    else
        parent->right = NULL;

    free(last);

    /* Restore Max Heap property */
    heapify_down(*root);

    return (extracted_value);
}
