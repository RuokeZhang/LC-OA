'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
'''
head = [1,2,3,2,1]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
def convertToList(nums):
    dummy=ListNode(0)
    cur=dummy
    for x in nums:
        cur.next=ListNode(x)
        cur=cur.next
    return dummy.next

def reverseList(list):
    pre=None
    cur=list
    #1->2->3
    while cur:
        nxt=cur.next
        cur.next=pre
        pre=cur
        cur=nxt
    return pre

def isPalindrome(head):
    head=convertToList(head)
    slow=fast=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    list2=slow #3,2,1
    list2=reverseList(list2)

    #head=1,2,3,2,1
    #list2=1,2,3
    while list2:
        if head.val!=list2.val:
            return False
        list2=list2.next
        head=head.next
    return True

print(isPalindrome(head))