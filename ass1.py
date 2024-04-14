class PriorityQueueNode:
    def __init__(self, id, name, priority) -> None:
        self.id = id
        self.name = name
        self.priority = priority
        self.next = None
        self.prev = None 
    
    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(self.priority)

class PriorityQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 
        self.next_id = 1

    def get_next_id(self):
        id = self.next_id
        self.next_id += 1
        return id
    
    def is_empty(self):
        return self.head is None

    def insert(self, name, priority):
        new_node = PriorityQueueNode(self.get_next_id(), name, priority)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            iter = self.head 
            while iter is not None and iter.priority < priority:
                iter = iter.next
            if iter is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                if iter == self.head:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                else:
                    iter.prev.next = new_node
                    new_node.prev = iter.prev
                    iter.prev = new_node
                    new_node.next = iter

    def remove(self):
        if self.is_empty():
            return None, None, None
        else:
            temp = self.tail
            if self.tail == self.head:  
                self.tail = None
                self.head = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return temp.id, temp.name, temp.priority

    def peek(self):
        if self.is_empty():
            return None, None, None
        else:
            return self.tail.id, self.tail.name, self.tail.priority

    def change_priority(self, id, priority):
        iter = self.head
        while iter is not None:
            if iter.id == id:
                iter.priority = priority
                break
            iter = iter.next

    def traverse(self):
        if self.is_empty():
            print("Empty Queue")
        else:
            iterator = self.head
            while iterator is not None:
                print(iterator)
                iterator = iterator.next


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("Flight 345", 1)
    pq.insert("Flight 190", 3)
    pq.insert("Flight 188", 7)
    pq.insert("Flight 621", 0)
    pq.insert("Flight 511", 5)
    pq.insert("Flight 810", 3)
    pq.traverse()

    # Simulating flight control
    while not pq.is_empty():
        id, name, priority = pq.remove()
        if "Emergency" in name:
            print(f"CONTROL: {name} land (EMERGENCY)")
        else:
            print(f"CONTROL: {name} land")
