#include "lists.h"

/**
 * check_cycle - find cycle in list
 * @list: list
 *
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list->next;
	hare = list->next->next;

	while (hare)
	{
		if (tortoise == hare)
			return (1);

		tortoise = tortoise->next;
		if (hare->next == NULL)
			return (0);
		hare = hare->next->next;
	}

	return (0);
}
