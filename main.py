from myclass import Person
from linked_class import Queue

def personQueue():
    print("Queue")
    for q in personQueue:
        print(q)

personQueue = Queue()
print("checker to dequeue an empty queue")
personQueue.dequeue()

first = Person('Bayan', 20, 'Harry Potter')
second = Person('Zhaniya', 22, 'Jane Eyre')
third = Person('Farida', 23, 'Naruto')

personQueue.enqueue(first)
personQueue.enqueue(second)
personQueue.enqueue(third)

for q in personQueue:
    print(q)
