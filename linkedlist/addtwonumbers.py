# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1 = []
    while(l1):
        num1.append(l1.val)
        if l1.next: l1 = l1.next
        else: break
    num2 = []
    while(l2):
        num2.append(l2.val)
        if l2.next:l2 = l2.next
        else:break
    print("Logged numbers are",num1, num2)
    
    if len(num2) >= len(num1): longer_list, shorter_list = num2, num1;
    else: longer_list, shorter_list = num1, num2;
    i = len(longer_list)
    j = len(shorter_list)
    
    # Find Sum
    sum = [0 for i in range(i+1)]
    for k in range(0, i):
        if j-k > 0:
            temp_sum = longer_list[k] + shorter_list[k]
            sum[k]+= temp_sum
            if sum[k] > 9:
                sum[k+1] += int(sum[k]/10)
                sum[k] = int(sum[k]%10)
        else:
            sum[k]+= longer_list[k]
            if sum[k]>9:
                sum[k+1] += int(sum[k]/10)
                sum[k] = int(sum[k]%10)
        print("sum", sum)
    if sum[i]!=0: 
        i = i+1;
    # Make Linked list
    prev = ListNode()
    beg = prev
    prev.val = sum[0]
    for k in range(1,i):
        new_node = ListNode()
        new_node.val = sum[k]
        prev.next = new_node
        prev = prev.next
    return beg





list1 = [1,2,3,4]
list2 = [1,1,1]
print("Input numbers are", list1, list2)

l1 = ListNode()
temp = l1

for i in range(0, len(list1)-1):
    temp.val = list1[i]
    next_temp = ListNode()
    temp.next = next_temp
    temp = temp.next
temp.val = list1[i+1]
temp.next = None

l2 = ListNode()
temp = l2

for i in range(0, len(list2)-1):
    temp.val = list2[i]
    next_temp = ListNode()
    temp.next = next_temp
    temp = temp.next
temp.val = list2[i+1]
temp.next = None

l3 = addTwoNumbers(l1,l2)
while(l3):
    l3 = l3.next