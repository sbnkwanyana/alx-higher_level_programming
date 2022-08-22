#include "lists.h"
/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: singly linked list
 * Return: (int) 1 if found, 0 if not found
 */
int check_cycle(listint_t *list)
{
	listint_t *move_once;
	listint_t *move_twice;

	move_once = malloc(sizeof(listint_t));
	move_twice = malloc(sizeof(listint_t));
	move_once = list;
	move_twice = list;

	while (move_once && move_twice && move_twice->next)
	{
		move_once = move_once->next;
		move_twice  = move_twice->next->next;
		if (move_once == move_twice)
		{
			free(move_once);
			free(move_twice);
			return (1);
		}
	}
	free(move_once);
	free(move_twice);
	return (0);
}
