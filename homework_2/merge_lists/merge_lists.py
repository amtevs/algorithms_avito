class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_with_dummy(list1, list2):
    dummy = ListNode()
    curr = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1 is not None:
        curr.next = list1
    else:
        curr.next = list2
    return dummy.next
    
def merge_without_dummy(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    curr = head
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1 is not None:
        curr.next = list1
    else:
        curr.next = list2
    return head