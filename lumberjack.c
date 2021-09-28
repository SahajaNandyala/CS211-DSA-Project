#include<stdio.h>
#include<stdlib.h>
#include "LinkedList.h"


int main()
{
    struct tree_prop *tree_prop;
	int time_limit, grid_size,no_of_trees;
	int i;

    // taking time limit, grid size and number of trees as input
	scanf("%d %d %d", &time_limit, &grid_size, &no_of_trees);

    // taking input of each tree properties
    for(i=0;i<no_of_trees;i++)
	{

        tree_prop = (struct tree_prop*)malloc(sizeof(struct tree_prop));
		scanf("%d %d %d %d %d %d",&tree_prop->x, &tree_prop->y, &tree_prop->h, &tree_prop->d, &tree_prop->c, &tree_prop->p);
		tree_prop->value = tree_prop->p * tree_prop->h * tree_prop->d;
		tree_prop->weight = tree_prop->c * tree_prop->d * tree_prop->h;
		tree_prop->price = tree_prop->value;
        insert(tree_prop);
	}
    display();

    printf("********\n");
    int time = 0;
    while (time < time_limit)
    {
    	int min, total_price = 0, position;
    	min = head->x + head->y;

    	//To find the nearest tree
    	for(i=0;i<no_of_trees;i++)
        {
            if(tree_prop->x + tree_prop->y < min)
            {
                min = tree_prop->x + tree_prop->y;
                position = i;
                tree_prop = tree_prop -> next;
            }
        }

        //Checking whether the time limit given is sufficient to go to that tree and cut that tree
        if(tree_prop->x + tree_prop->y + tree_prop->d < time_limit)
        {
            total_price = total_price + tree_prop->price;
        }

    }
	return 0;

}
