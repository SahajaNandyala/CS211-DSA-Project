#include<stdio.h>
#include<stdlib.h>

struct tree
{
    int x,y,h,d,c,p;
    int value,weight;
    
};

int main()
{
    struct tree *tree_prop;
	int time_limit,grid_size,no_of_trees;
	int i;
	scanf("%d%d%d",&time_limit,&grid_size,&no_of_trees);
	tree_prop=(struct tree*)malloc(no_of_trees*sizeof(struct tree));
	for(i=0;i<no_of_trees;i++)
	{
		scanf("%d %d %d %d %d %d",&tree_prop[i].x,&tree_prop[i].y,&tree_prop[i].h,&tree_prop[i].d,&tree_prop[i].c,&tree_prop[i].p);
		tree_prop[i].value=tree_prop[i].p*tree_prop[i].h*tree_prop[i].d;
		tree_prop[i].weight=tree_prop[i].c*tree_prop[i].d*tree_prop[i].h;		
	}	
	return 0;

}

