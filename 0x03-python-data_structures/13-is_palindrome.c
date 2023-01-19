#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * list_len - Compute length of list
 * @h: list
 *
 * Return: length of list
 */
static size_t list_len(const listint_t *h)
{
	size_t len = 0;

	while (h)
	{
		h = h->next;
		len++;
	}

	return (len);
}

/**
 * build_int_array_from_list - Builds int array from list
 * @arr: int array buffer
 * @h: list
 *
 */
static void build_int_array_from_list(int *arr, const listint_t *h)
{
	size_t i = 0;

	while (h)
	{
		arr[i] = h->n;
		h = h->next;
		i++;
	}
}

/**
 * is_palindrome_helper - Checks if a list is palindrome
 * @arr: int array
 * @start: index of start
 * @end: index of end
 *
 * Return: 1 if the list is palindrome, 0 otherwise
 */
int is_palindrome_helper(int *arr, int start, int end)
{
	if (start >= end)
		return (1);

	if (*(arr + start) != *(arr + end))
		return (0);

	return (is_palindrome_helper(arr, start + 1, end - 1));
}

/**
 * is_palindrome - Checks if a list is palindrome
 * @head: list
 *
 * Return: 1 if the list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t n = 0;
	int *intArray, ret;

	n = list_len(*head);
	if (n == 0)
		return (1);

	intArray = (int *)malloc(n * sizeof(int));
	if (intArray == NULL)
		return (0);
	build_int_array_from_list(intArray, *head);

	ret = is_palindrome_helper(intArray, 0, n - 1);

	free(intArray);
	return (ret);
}
