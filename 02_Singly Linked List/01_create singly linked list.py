class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class SLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        # empty 
        if self.head is None:
            self.head = new_node
            return

        # 1 node
        if self.head.next is None:
            self.head.next = new_node
            return
    
        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = new_node
        return
    
    def revers(self):
        prev = None
        cur_node = self.head
        while cur_node:
            next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next
        self.head = prev
        

    def print_nodes(self):
        cur_node = self.head
        
        while cur_node is not None:
            print(cur_node.data, end = "->")
            cur_node = cur_node.next

        print("None")
 
sll = SLL()
sll.insert_at_beginning(10)
sll.insert_at_beginning(20)
sll.print_nodes()
sll.revers()
sll.print_nodes()

sll1 = SLL()
sll1.insert_at_end(10)
sll1.insert_at_end(20)
sll1.print_nodes()
sll1.revers()
sll1.print_nodes()

