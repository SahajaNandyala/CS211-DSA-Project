#include<stdlib.h>
#include <stdio.h>

void insert();
void delete();

struct tree_prop
{
    int x, y, h, d, c, p;
    int value, weight, price;
    struct tree_prop *next;
};
struct tree_prop *head = NULL;

void insert(struct tree_prop *newnode)
{
    struct tree_prop *tail;
    newnode -> next = NULL;

    if(head == NULL)
    {
        head = newnode;
    }
    else
    {
        tail = head;
        while(tail->next !=NULL)
        {
            tail = tail->next ;
        }
        tail->next = newnode;
    }
}

void delete(int pos)
{
    int i;
    struct tree_prop *position,*positionprevnode;
    if(head==NULL)
    {
        exit(0);
    }
    else
    {

        if(pos==0)
        {
            position = head;
            head = head->next ;
            free(position);
        }
        else
        {
            position = head;
            for(i=0;i<pos;i++)
            {
                positionprevnode = position;
                position = position->next;
                if(position==NULL)
                {
                    return;
                }
            }
            positionprevnode->next =position->next ;
            free(position);
        }
    }
}

// display function
void display()
{
    struct tree_prop *traversal;
    if(head==NULL)
    {
        printf("\n List is empty:\n");
        return;
    }
    else
    {
        traversal=head;
        printf("\nThe List elements are:\n");
        while(traversal -> next != NULL)
        {
                printf("%d\n",traversal->x);
                traversal=traversal->next ;
        }
        printf("%d\n",traversal->x); //To print the last element before it moves back to head
        return;
    }

}
