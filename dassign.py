#queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)



#stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()



#queue using two stack
class Queue1:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def is_empty(self):
        return (self.inbox.is_empty() and self.outbox.is_empty())

    def enqueue(self, data):
        self.inbox.push(data)

    def dequeue(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                popped = self.inbox.pop()
                self.outbox.push(popped)
        return self.outbox.pop()


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()




#stack using queue
class Stack1:
    def __init__(self):
        self.q = Queue()

    def is_empty(self):
        return self.q.is_empty()

    def push(self, data):
        self.q.enqueue(data)

    def pop(self):
        for _ in range(self.q.get_size() - 1):
            dequeued = self.q.dequeue()
            self.q.enqueue(dequeued)
        return self.q.dequeue()


class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.size += 1
        self.items.append(data)

    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)

    def get_size(self):
        return self.size




####list


class check():
    def __init__(self):
        self.n = []

    def add(self, a):
        return self.n.append(a)

    def remove(self, b):
        self.n.remove(b)

    def dis(self):
        return (self.n)




#create and display linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next









if __name__ == '__main__':
    choice = 1
    while choice != 7:
        print('what you want to do')
        print('1. queue')
        print('2. stack')
        print('3. queue using stack')
        print('4. stack using queue')
        print('5. List')
        print('6. Linked list')
        print('7. exit')

        choice = int(input("Enter choice: "))
        if choice == 1:
            q = Queue()

            while True:
                print('enqueue <value>')
                print('dequeue')
                print('quit')
                do = input('What would you like to do? ').split()

                operation = do[0].strip().lower()
                if operation == 'enqueue':
                    q.enqueue(int(do[1]))

                   #q.enqueue(int(input("Enter the number to enqueue")))
                elif operation == 'dequeue':
                    if q.is_empty():
                        print('Queue is empty.')
                    else:
                        print('Dequeued value: ', q.dequeue())
                elif operation == 'quit':
                    break

        elif choice == 2:
            s = Stack()
            while True:
                print('push <value>')
                print('pop')
                print('quit')
                do = input('What would you like to do? ').split()

                operation = do[0].strip().lower()
                if operation == 'push':
                    s.push(int(do[1]))
                elif operation == 'pop':
                    if s.is_empty():
                        print('Stack is empty.')
                    else:
                        print('Popped value: ', s.pop())
                elif operation == 'quit':
                    break

        elif choice == 3:
            a_queue = Queue()
            while True:
                print('enqueue <value>')
                print('dequeue')
                print('quit')
                do = input('What would you like to do? ').split()

                operation = do[0].strip().lower()
                if operation == 'enqueue':
                    a_queue.enqueue(int(do[1]))
                elif operation == 'dequeue':
                    if a_queue.is_empty():
                        print('Queue is empty.')
                    else:
                        dequeued = a_queue.dequeue()
                        print('Dequeued element: ', int(dequeued))
                elif operation == 'quit':
                    break
        elif choice == 4:
            s = Stack()


            while True:
                print('Menu')
                print('push <value>')
                print('pop')
                print('quit')

                do = input('What would you like to do? ').split()

                operation = do[0].strip().lower()
                if operation == 'push':
                    s.push(int(do[1]))
                elif operation == 'pop':
                    if s.is_empty():
                        print('Stack is empty.')
                    else:
                        print('Popped value: ', s.pop())
                elif operation == 'quit':
                    break

        elif choice == 5:
            obj = check()

            choice = 1
            while choice != 0:
                print("0. Exit")
                print("1. Add")
                print("2. Delete")
                print("3. Display")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    n = int(input("Enter number to append: "))
                    obj.add(n)
                    print("List: ", obj.dis())

                elif choice == 2:
                    n = int(input("Enter number to remove: "))
                    obj.remove(n)
                    print("List: ", obj.dis())

                elif choice == 3:
                    print("List: ", obj.dis())
                elif choice == 0:
                    print("Exiting!")
                else:
                    print("Invalid choice!!")

            print()
        elif choice == 6:
            a_llist = LinkedList()
            n = int(input('How many elements would you like to add? '))
            for i in range(n):
                data = int(input('Enter data item: '))
                a_llist.append(data)
            print('The linked list: ', end='')
            a_llist.display()


        elif choice == 7:
            print("Exiting!")
        else:
            print("Invalid choice!!")
