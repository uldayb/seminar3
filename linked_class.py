from myboxiterator import MyBoxIterator

class Queue:
    def __init__(self):
        self._theItems = list()

    def __len__(self):
        return len(self._theItems)

    def enqueue(self, item):
        self._theItems.append(item)

    def dequeue(self):
        try:
            self._theItems[0]
        except IndexError:
            print('Queue is empty, cannot be done!')
        else:
            return self._theItems.pop(0)

    def __contains__(self, item):
        return item in self._theItems

    def __iter__(self):
        return MyBoxIterator(self._theItems)
