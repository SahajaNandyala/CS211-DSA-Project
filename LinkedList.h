#include<stdlib.h>
#include <stdio.h>

void insert();
void delete();

struct node
{
        int data;
        struct node *next;
};
struct node *head = NULL;

void insert(struct node *newnode)
{
    struct node *tail;

    if(head == NULL)
    {
        head = newnode;
        newnode -> next = NULL;
    }
    else
    {
        tail = head;
        while(tail->next !=NULL)
        {
            tail = tail->next ;
        }
        tail->next = newnode;
        newnode -> next = NULL;
    }
}

void delete(int pos)
{
    int i;
    struct node *position,*positionprevnode;
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
            position=head;
            for(i=0;i<pos;i++)
            {
                positionprevnode = position;
                position=position->next;
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
