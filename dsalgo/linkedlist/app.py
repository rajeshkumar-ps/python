class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def appendAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")     

ll = LinkedList()
ll.appendAtFront(10)
ll.appendAtFront(20)
ll.appendAtFront(30)
ll.display()
      