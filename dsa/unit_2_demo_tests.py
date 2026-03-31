from unit_2_lineards import DynamicArray, SinglyLinkedList, Stack, Queue, is_balanced
def demo():
    for N in [5,10,20]:
        print(f"Testing DynamicArray with N={N}")
        arr = DynamicArray()
        for i in range(N):
            arr.append(i)
            print(f"Appended {i}, size now {arr.size}")
            print(f"array capacity: {arr.capacity}")
demo()

# T1. DynamicArray
print("T1. DynamicArray")

arr = DynamicArray()

print("Append operations:")
for x in [1, 2, 3, 4, 5]:
    arr.append(x)
    print(f"Appended {x} → size={arr.size()}, capacity={arr.capacity()}")

# Pop twice
arr.pop()
arr.pop()

# Print remaining elements
remaining = [arr.get(i) for i in range(arr.size())]
print("After 2 pops:", remaining)

# Insert and delete
arr.insert(1, 99)
arr.delete(2)

final_list = [arr.get(i) for i in range(arr.size())]
print("Final list:", final_list)


# T2. Singly Linked List

print("\nT2. Singly Linked List")

ll = SinglyLinkedList()

# Insert at beginning: 3,2,1
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)

# Insert at end: 4,5
ll.insert_at_end(4)
ll.insert_at_end(5)

print("Traverse:", ll.traverse())  # expected: [1,2,3,4,5]

# Delete 3
ll.delete_by_value(3)
print("After deleting 3:", ll.traverse())  # expected: [1,2,4,5]

# Search
print("Search 4:", "Found" if ll.search(4) != -1 else "Not Found")
print("Search 100:", "Found" if ll.search(100) != -1 else "Not Found")


# T3. Stack

print("\nT3. Stack")

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Peek:", s.peek())  # expected: 30

s.pop()
s.pop()

print("Peek after 2 pops:", s.peek())  # expected: 10

# T4. Queue
print("\nT4. Queue")

q = Queue()

q.enqueue(7)
q.enqueue(8)
q.enqueue(9)

print("Front:", q.front())  # expected: 7

q.dequeue()
q.dequeue()

print("Front after 2 dequeues:", q.front())  # expected: 9

# T5. Parentheses Checker
print("\nT5. Parentheses Checker")

tests = ["([])", "([)]", "(((", ""]

for t in tests:
    print(f"{t!r} → {is_balanced(t)}")
