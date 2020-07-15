"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        if not self.head == None:
            return Element(new_element)
        temp = Element(new_element)
        temp.next = self.head
        self.head = temp
        # return head
        # pass

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head == None:
            return None
        if self.head.next == None:
            self.head = None
            return None
        temp1 = self.head.value
        self.head.next = self.head
        return temp1
        # pass

class stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        if self.ll == None:
            self.ll = Element(new_element)
        else:
            temp = Element(new_element)
            temp.next = self.ll
            self.ll = temp
        # pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        next = self.next
        if self.ll == None:
            return None
        else:
            temp1 = self.ll
            self.ll = self.ll.next
            self.ll.next = None
            return temp1.value
        pass
    