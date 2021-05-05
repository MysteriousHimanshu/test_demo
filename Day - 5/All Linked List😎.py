class Node:
    
    def __init__(self, x):
        self. data = x 
        self. next = None 
    
class LinkedList(object):
    
    def __init__(self):
        self. head = None 
    
    def addNode(self, data):
        if self. head is None:
            self. head = Node(data) 
        else:
            
            temp = Node(data) 
            temp.next = self.head 
            self. head = temp 
    
    def printList(self):
        temp = self. head 
        
        while temp != None:
            print(temp. data, end = " ")
            temp = temp.next 
        print()
        
    def reverseList(self):
        prev = None 
        curr = self. head 
        next = None 
        while curr != None:
            
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        self. head = prev 
        self. printList()
    
    def findMiddle(self):
        if self. head is None or self. head. next is None:
            return self. head.data 
        slow = self. head 
        fast = self. head
        while fast != None and fast .next !=  None:
            slow = slow.next 
            fast = fast.next.next  
        
        print(slow.data)
            
    def merge(self, A, B):
        if A is None: return B 
        if B is None: return A 
        
        result = None 
        
        if A. data < B.data:
            result = A 
            result.next = self. merge(A. next, B) 
        
        else:
            result = B 
            result.next = self.merge(A, B.next)
        
        return result
    
    def calculate_length(self):
        count = 0 
        temp = self. head
        
        while temp != None:
            
            count += 1 
            temp = temp.next 
        
        return count 
            
    def deleteNthNode(self, N): #2pass 
        temp = self.head 
        length = self. calculate_length()
        if length == N:
            return temp.next 
        
        diff = length - N 
        count  = 1 
        curr = self.head 
        while count != diff:
            count += 1 
            curr = curr.next 
        curr.next = curr.next.next 
        
        return temp 
        
    def deleteFromLast(self, N):
        print("n = ", N )
        slow = self. head 
        fast = self.head 
        for i in range(N):
            fast = fast.next 
        
        if fast == None:
            return self.head.next 
            
            
        while fast.next != None:
            slow = slow.next 
            fast = fast.next 
        slow.next = slow.next.next
        
        return self. head 
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None 
        head = None 
        
        carry = 0 
        while l1 or l2:
            
            sum = 0 
            if l1:
                sum += l1. val 
                l1 = l1. next 
                
            if l2:
                sum += l2. val 
                l2 = l2. next 
                
            sum = sum + carry 
            
            new_node = ListNode(sum % 10)
            carry = sum // 10 
            
            if result:
                
                result . next = new_node 
                result = result. next 
                
            else:
                
                result = head = new_node 
                
        if carry > 0:
            result. next = ListNode(carry) 
            
        return head  
    
    
                
                
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        pointA = headA
        pointB = headB
          
        
        while pointA != pointB:
            pointA = pointA.next
            pointB = pointB.next
            
            if pointA == pointB:
                return pointA
            
            if pointA is None:
                pointA = headB
                
            if pointB is None:
                pointB = headA
                
        return pointA
    
                                
                
        
def main():
    
    start1 = LinkedList() 
    for i in range(int(input())):
        start1. addNode(int(input()))
        
    # start2 = LinkedList()
    # for i in range(int(input())):
    #     start2. addNode(int(input()))
    

    # start1. printList() 
    # start2.printList()
    # # start.reverseList()
    # start.findMiddle()
    
    # start1.head  = start1.merge(start1.head, start2.head)
    start1.printList()
    dummy = LinkedList()
    dummy.head = start1.head
    # dummy.deleteNthNode(3)
    dummy .head = dummy.deleteFromLast(0) 
    dummy.printList()
    # print(dummy.head.data)
    
        
        
        
if __name__ == '__main__':
    main()
        