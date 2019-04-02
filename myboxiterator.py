class MyBoxIterator():

    def __init__( self, L ):
        self.L = L
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.L):
            item = self.L[self.index]
            self.index = self.index + 1
            return item

        else:
            raise StopIteration
