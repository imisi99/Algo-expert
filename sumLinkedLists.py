# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # looping through the first linkedlist
    sum = ''
    sum1 = ''
    current = linkedListOne
    current1 = linkedListTwo
    while current or current1:
        if current:
            val = str(current.value)
            sum = sum + val
            current = current.next
        if current1:
            val = str(current1.value)
            sum1 = sum1 + val
            current1 = current1.next
    
    sum = int(sum[::-1]) + int(sum1[::-1])
    sum = str(sum)
    
    new_list = LinkedList(int(sum[-1]))
    current = new_list
    
    i = len(sum) - 2
    while i >= 0:
        current.next = LinkedList(int(sum[i]))
        current = current.next
        
        i -= 1
         
    return new_list
