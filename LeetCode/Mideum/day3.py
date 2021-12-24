# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        num3 = []
        exit = 0
        
        while(exit!=1):
            num1.append(l1.val)
            if l1.next == None:
                exit = 1
            else:
                l1 = l1.next

        exit=0            

        while(exit!=1):
            num2.append(l2.val)
            if l2.next == None:
                exit = 1
            else:
                l2 = l2.next
        
        if len(num1) > len(num2):
            k = len(num1)-len(num2)
            for i in range(k):
                num2.append(0)
        elif len(num1) < len(num2):
            k = len(num2)-len(num1)
            for i in range(k):
                num1.append(0)
        
        stack = 0
        for j in range(len(num1)):
            if num1[j]+num2[j]>=10 and stack ==0:
                num3.append(num1[j]+num2[j]-10)
                stack = 1
            elif num1[j]+num2[j]>=9 and stack ==1:
                num3.append(num1[j]+num2[j]-10 +1)
                stack = 1
            elif num1[j]+num2[j] < 10 and stack ==0:
                num3.append(num1[j]+num2[j])
                stack = 0
            elif num1[j]+num2[j] < 9 and stack ==1:
                num3.append(num1[j]+num2[j]+1)
                stack = 0
            if j==len(num1)-1 and stack ==1:
                num3.append(1)
        print(num3)
        
        l3 = ListNode(num3[0], None)   
        head = l3
        for jj in range(1, len(num3)):
            l3.next = ListNode(num3[jj])
            l3 = l3.next
        return head
        
