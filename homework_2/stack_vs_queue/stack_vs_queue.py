class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Mystack:
    def __init__(self):
        self.head = None

    def push(self, x: int):
        n = ListNode(x, self.head) 
        self.head = n
        
    def pop(self) -> int:
        if self.head is None:
            return None
        v = self.head.val
        self.head = self.head.next
        return v

    def peek(self) -> int:
        if self.head is None:
            return None
        return self.head.val

    def empty(self) -> bool:
        return self.head== None      
        
        
class MyQueue:
    def __init__(self):
        self.last = None
        self.first = None
        
    def enqueue(self, x: int):
        if self.first is None:
            n = ListNode(x)
            self.last = n
            self.first = n
        else:
            n = ListNode(x)
            self.last.next=n
            self.last=n
        
    def dequeue(self):
        if self.first is None:
            return None
        if self.first.next is None:
            v= self.first.val
            self.last = None
            self.first = None
            return v
        v= self.first.val
        self.first=self.first.next
        return v
        
    def empty(self):
        return self.first== None 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        