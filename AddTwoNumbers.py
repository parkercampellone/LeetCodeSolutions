# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.convertToNumber(l1)
        num2 = self.convertToNumber(l2)
        finalNum = num1 + num2
        nodeList = self.convertToListNode(finalNum)

        return nodeList

    def convertToNumber(self, nodeList: ListNode):
        currNode = nodeList
        number = 0
        while currNode is not None:
            number = number * 10 + currNode.val
            currNode = currNode.next
        
        return int(str(number)[::-1])
    
    def convertToListNode(self, number: int):
        numList = [int(digit) for digit in str(number)]
        numList.reverse()
        prevNode = None
        rootNode = None
        for num in numList:
            node = ListNode(num)
            if prevNode == None:
                prevNode = node
                rootNode = node
                continue
            else:
                prevNode.next = node
                prevNode = node
        return rootNode



