class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
 
 
class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
 
    def size(self):
     current = self.head
     count = 0
     while current:
        count += 1
        current = current.next_node
     return count
       
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data, " -> ", end = '') 
            temp = temp.next_node
        print("")
 
    def insert_at_head(self, data):
      new_node = Node(data)
      new_node.next_node = self.head
      self.head = new_node
 
    def get_next_node (self,node):
      return node.next_node.data
    

def mergeLinkedList(llist1, llist2):
    pointer1 = llist1.head
    pointer2 = llist2.head
    head1 = pointer1
    while pointer1.next_node != None and pointer2.next_node != None:
        if pointer1.data <= pointer2.data:
            if pointer1.next_node.data >= pointer2.data:
                tmp = pointer1.next_node
                pointer1.next_node = pointer2
                pointer2 = pointer2.next_node
                pointer1 = pointer1.next_node
                pointer1.next_node = tmp
            else:
                pointer1 = pointer1.next_node
        else:
            pass
    print(pointer1.data, pointer2.data)
    llist1.printList()
    if pointer2.next_node == None:
        if pointer2.data >= pointer1.data:
            while pointer2.data >= pointer1.data and pointer1.next_node != None:
                if pointer1.next_node.data >= pointer2.data:
                    tmp = pointer1.next_node
                    pointer1.next_node = pointer2
                    pointer2.next_node = tmp
                    break
                pointer1 = pointer1.next_node
            pointer1.next_node = pointer2
        else:
            tmp = pointer1
            pointer1 = pointer2
            pointer1.next_node = tmp
    elif pointer1.next_node == None:
        if pointer2.data >= pointer1.data:
            pointer1.next_node = pointer2
        else:
            while pointer1.data >= pointer2.data and pointer2.next_node != None:
                tmp = pointer1
                pointer1 = pointer2
                pointer1.next_node = tmp
                pointer1 = pointer1.next_node
                pointer2 = pointer2.next_node
            pointer1.next_node = pointer2     
    print(pointer1.data, pointer2.data)
    return llist1


llist1 = LinkedList()
llist2 = LinkedList()
llist1.head = Node(1)
llist2.head = Node(2)
s = Node(3)
t = Node(5)
l = Node(7)
a = Node(4)
b = Node(6)
c = Node(8)
llist2.head.next_node = s
s.next_node = t
t.next_node = l
l.next_node = None
llist1.head.next_node = a
a.next_node = b
b.next_node = c
c.next_node = None
llist1.printList()
llist2.printList()
if llist1.head.data <= llist2.head.data:
    mergeLinkedList(llist1, llist2).printList()
else:
    mergeLinkedList(llist2, llist1).printList()
llist3 = LinkedList()
llist3.head = Node(1)
llist3.head.next_node = Node(2)
llist4 = LinkedList()
llist4.head = Node(3)
llist4.head.next_node = Node(4)
mergeLinkedList(llist3, llist4).printList()