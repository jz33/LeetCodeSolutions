typedef struct ListNode node;
node* swapPairs(node* even)
{
    node *prev = 0, *oddy, *next, *ret;
    if(even == 0 || even->next == 0) return even;
    
    ret = even->next;
    prev = ret;
    
    while(even != 0 && even->next != 0)
    {
        oddy = even->next;
        next = oddy->next;
        
        prev->next = oddy;
        oddy->next = even;
        
        prev = even;
        even = next;
    }
    prev->next = even;
    return ret;
}
