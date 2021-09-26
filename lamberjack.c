#include<stdio.h>
#include<stdlib.h>
#include "LinkedList.h"

struct tree
{
    int x, y, h, d, c, p;
    int value, weight, price;

};

int main()
{
    struct tree *tree_prop;
	int time_limit, grid_size,no_of_trees;
	int i;

    insert();
    display();
    // taking time limit, grid size and number of trees as input
	scanf("%d %d %d", &time_limit, &grid_size, &no_of_trees);

    // array of trees
	tree_prop = (struct tree*)malloc(no_of_trees*sizeof(struct tree));

    // taking input of each tree properties
    for(i=0;i<no_of_trees;i++)
	{
		scanf("%d %d %d %d %d %d",&tree_prop[i].x, &tree_prop[i].y, &tree_prop[i].h, &tree_prop[i].d, &tree_prop[i].c, &tree_prop[i].p);
		tree_prop[i].value = tree_prop[i].p * tree_prop[i].h * tree_prop[i].d;
		tree_prop[i].weight = tree_prop[i].c * tree_prop[i].d * tree_prop[i].h;
		tree_prop[i].price = tree_prop[i].value;
	}

    int time = 0;
    while (time < time_limit)
    {
    	int min, total_price = 0, position;
    	min = tree_prop[0].x + tree_prop[0].y;

    	//To find the nearest tree
    	for(i=0;i<no_of_trees;i++)
        {
            if(tree_prop[i].x + tree_prop[i].y<min)
            {
                min = tree_prop[i].x + tree_prop[i].y;
                position = i;
            }
        }

        //Checking whether the time limit given is sufficient to go to that tree and cut that tree
        if(tree_prop[position].x + tree_prop[position].y + tree_prop[position].d < time_limit)
        {
            total_price = total_price + tree_prop[position].price;
        }

    }
	return 0;

}
