class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.data = [None] * self.capacity

    def append(self,value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1
    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty array")
        value = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return value
    def get(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        return self.data[index]
    def set(self,index,value):
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        self.data[index] = value
    def insert(self,index,value):
        if index < 0 or index > self.size:
            raise IndexError("index out of bounds")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1
    def delete(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1
    def size(self):
        return self.size
    def _resize(self,new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def delete_by_value(self,x):
        temp = self.head
        prev = None
        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next
    def search(self,x):
        temp = self.head
        while temp:
            if temp.data == x:
                return True
            temp = temp.next
        return False
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, x):
        new_node = DNode(x)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after_node(self, key, x):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            return False 

        new_node = DNode(x)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

        return True

    def delete_at_position(self, pos):
        if self.head is None or pos < 0:
            return False

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return True

        for _ in range(pos):
            temp = temp.next
            if temp is None:
                return False  # position out of bounds

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        return True

    def traverse(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result
class Stack:
    def __init__(self):
        self.head = None  # top of stack
        self._size = 0

    # Push (insert at beginning)
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    # Pop (remove from beginning)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        val = self.head.data
        self.head = self.head.next
        self._size -= 1
        return val

    # Peek (top element)
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.head.data

    # Check if empty
    def is_empty(self):
        return self.head is None

    # Optional: size
    def size(self):
        return self._size
class Queue:
    def __init__(self):
        self.head = None  # front
        self.tail = None  # rear
        self._size = 0

    # Enqueue (insert at end)
    def enqueue(self, x):
        new_node = Node(x)

        if self.tail is None:  # empty queue
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    # Dequeue (remove from front)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        val = self.head.data
        self.head = self.head.next

        if self.head is None:  # queue became empty
            self.tail = None

        self._size -= 1
        return val

    # Front element
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.data

    # Check if empty
    def is_empty(self):
        return self.head is None

    # Optional size
    def size(self):
        return self._size
def is_balanced(s):
    stack = Stack()

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        # If opening bracket → push
        if ch in "({[":
            stack.push(ch)

        # If closing bracket → check
        elif ch in ")}]":
            if stack.is_empty():
                return False  # nothing to match

            top = stack.pop()

            if top != pairs[ch]:
                return False  # mismatch

    # At end, stack must be empty
    return stack.is_empty()
