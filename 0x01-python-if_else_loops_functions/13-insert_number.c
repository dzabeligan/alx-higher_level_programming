#include "lists.h"

/**
 * insert_node - Insert a number into a sorted singly-linked list
 * @head: pointer to the head of the linked list
 * @number: number to insert
 *
 * Return: If the function fails - NULL, otherwise, pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newNode;

	newNode = (listint_t *)malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	if (node == NULL || node->n >= number)
	{
		newNode->next = node;
		*head = newNode;
		return (newNode);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	newNode->next = node->next;
	node->next = newNode;

	return (newNode);
}
